from enum import Enum


class APIScope(Enum):
    """ Allows read/write access to the user's sheets and their properties """
    SPREADSHEETS = 'https://www.googleapis.com/auth/spreadsheets'
