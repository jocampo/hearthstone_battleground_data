import csv
from datetime import datetime
import os

import deprecation

from entities import BattlegroundMatchLog


class FileLoader(object):
    """
    Loads the data file into the bg match log structure
    """
    def __init__(self, file_path, file_name):
        assert file_path
        assert file_name
        self.__file_path = file_path
        self.__file_name = file_name

    @deprecation.deprecated("Deprecated for the newer data file formats", details="Use load_file instead")
    def old_load_file(self):
        fixed_rows = []
        with open(f"{self.__file_path}/{self.__file_name}", "r") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                if len(row) == 2:
                    starting_mmr = int(row[1])
                    date = f'{row[0]}/{self.YEAR}'
                else:
                    bg = BattlegroundMatchLog(*[date, starting_mmr, *row])
                    fixed_rows.append(bg)
                    starting_mmr += int(bg.mmr_delta)
            file.close()
        return fixed_rows

    def load_file(self):
        fixed_rows = []
        with open(f"{self.__file_path}/{self.__file_name}", "r") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                if row[0] and row[0][0] == "#":
                    # Skip comments
                    continue
                fixed_rows.append(BattlegroundMatchLog(*row))
            file.close()
        return fixed_rows

    def version_file(self):
        """
        Once we're done with a data file, we can rename it with the current date and create a new data file
        with an example of the format that has to be followed.
        """
        today = datetime.today().strftime("%Y%m%d")
        versioned_file_name = f"test{today}_{self.__file_name}"
        os.rename(f"{self.__file_path}/{self.__file_name}", f"{self.__file_path}/{versioned_file_name}")
        with open(f"{self.__file_path}/{self.__file_name}", "w") as file:
            file.write(self.EXAMPLE_TEXT_FORMAT)
            file.close()

    # Data dump has no year, so we'll just hardcode that for now
    YEAR = 2021

    EXAMPLE_TEXT_FORMAT = "#7/4/2021;7271;7th;-83;Al'akir;tried to force beasts but nope;10;False"
