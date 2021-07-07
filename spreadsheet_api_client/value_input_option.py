from enum import Enum


class ValueInputOption(Enum):
    """
    The input is not parsed and is simply inserted as a string, so the input "=1+2" places the string "=1+2"
    in the cell, not a formula. (Non-string values like booleans or numbers are always handled as RAW.)
    """
    RAW = 'RAW'

    """
    The input is parsed exactly as if it were entered into the Google Sheets UI, so "Mar 1 2016" becomes a date,
    and "=1+2" becomes a formula. Formats may also be inferred, so "$100.15" becomes a number with currency formatting.
    """
    USER_ENTERED = 'USER_ENTERED'
