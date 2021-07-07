from file_loader import FileLoader
from spreadsheet_api_client.spreadsheet_handler import SpreadsheetHandler

PATH = "./res"
FILE_NAME = "bg_data.csv"

"""
    TODO List:
    - use logger
    - store data in db for additional structured usage
    - schedule this task somewhere to be done once per day? week? something.
    - setup some graphs in excel
    - come up with a front-end for this? m
"""

if __name__ == '__main__':
    fl = FileLoader(PATH, FILE_NAME)
    # bg_records = fl.old_load_file()
    bg_records = fl.load_file()

    if len(bg_records) == 0:
        raise Exception("No new BG records were found for upload. Exiting...")

    handler = SpreadsheetHandler()
    handler.dump_bg_data(bg_records)

    fl.version_file()
