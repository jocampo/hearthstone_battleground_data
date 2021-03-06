import functools
import os
import shutil

from db.AbstractDAO import AbstractDAO
from db.HeroDAO import HeroDAO
from db.MatchDAO import MatchDAO
from db.PlayerDAO import PlayerDAO
from db.entities.Hero import Hero
from db.entities.Match import Match
from db.entities.Player import Player
from entities import BattlegroundMatchLog
from file_loader import FileLoader
from spreadsheet_api_client.spreadsheet_handler import SpreadsheetHandler

PATH = "./res"
FILE_NAME = "bg_data.csv"

"""
    TODO List (eventually):
    - Set up a centralized logger
    - Client app that writes match data into file (look into hooking onto unity events)
    - Move data dump file into s3
    - Deploy db on a private instance
    - Setup a chron job to process the match logs every 24h
    - Deploy said service on a private instance
        - Fix less-than-happy scenarios and revert/not-commit db ops when upload fails?
        - Handle token expiring scenario
    - Leverage stats. Generate insights from data stored
        - Win-rate per hero
        - Look into comments for comps with best results
    - Add minion types per game (once data input is automated)
"""

def move_screenshots():
    """
    Utility method that really doesn't belong here :^)
    """
    name_pattern = "Hearthstone Screenshot"
    desktop_path = "C:\\Users\\jorge\\Desktop"
    ss_dir_name = "HS Screenshots"

    join_path_desktop = functools.partial(os.path.join, desktop_path)

    full_dir_path = join_path_desktop(ss_dir_name)
    if not os.path.isdir(full_dir_path):
        os.mkdir(full_dir_path)

    files = [f for f in os.listdir(desktop_path)
             if os.path.isfile(join_path_desktop(f))
             and f.startswith(name_pattern)]

    for file in files:
        shutil.move(join_path_desktop(file), join_path_desktop(ss_dir_name))


def store_player(player: Player):
    """
    For now this is the ONLY entry point for this entity (essentially hardcoded)
    """
    PlayerDAO.begin()
    PlayerDAO.create(player)
    PlayerDAO.commit()


def find_hero_id_in_pool(hero_name: str, heroes_pool: list[Hero]) -> int:
    """
    Given a list of heroes, we'll use the hero_name to determine if it's already present in the DB.
    If it does, we'll return the id, otherwise, -1
    :param hero_name: needle
    :param heroes_pool: haystack of heroes
    :return: -1 if the hero_name was not found, otherwise, the id of the corresponding hero in the db is returned
    """
    for hero in heroes_pool:
        if hero.name == hero_name:
            return hero.id
    return -1


def store_matches_db(records: list[BattlegroundMatchLog]):
    """
    Processes the bg match records and stores the data in the db
    :param records: bg match records list
    """
    player_id = 1  # hardcoded id, only have 1 for now
    current_mmr = 0

    # Hit DB once to request all heroes, we'll need this to determine when a hero already exists
    heroes = HeroDAO.list()

    AbstractDAO.begin()
    try:
        for record in records:
            hero_id = find_hero_id_in_pool(record.hero, heroes)
            if hero_id <= 0:
                hero = Hero()
                hero.name = record.hero

                HeroDAO.create(hero)

                hero = HeroDAO.get_by_name(record.hero)  # get the record we just inserted into the db
                heroes.append(hero)
                hero_id = hero.id

            match = Match()
            match.load_from_record(record)
            match.hero_id = hero_id
            match.player_id = player_id

            MatchDAO.create(match)
            current_mmr = int(record.starting_mmr) + int(record.mmr_delta)

        # Update the player's mmr with the last record's info
        player = PlayerDAO.get(player_id)
        player.current_mmr = current_mmr
        AbstractDAO.commit()
    except:
        AbstractDAO.rollback()
        raise
    finally:
        AbstractDAO.get_connection().close()


if __name__ == '__main__':
    fl = FileLoader(PATH, FILE_NAME)
    bg_records = fl.load_file()

    store_matches_db(bg_records)
    if len(bg_records) == 0:
        raise Exception("No new BG records were found for upload. Exiting...")

    handler = SpreadsheetHandler()
    handler.dump_bg_data(bg_records)

    fl.version_file()
