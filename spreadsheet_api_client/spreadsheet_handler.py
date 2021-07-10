from __future__ import print_function
import os.path
from typing import List

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from entities import BattlegroundMatchLog
from spreadsheet_api_client.scope import APIScope
from spreadsheet_api_client.value_input_option import ValueInputOption
from utils.singleton import Singleton


class SpreadsheetHandler(metaclass=Singleton):

    def __init__(self):
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        self.__service = build('sheets', 'v4', credentials=creds)

    def dump_bg_data(self, bg_data: List[BattlegroundMatchLog]):
        assert self.__service is not None

        values = [x.as_array() for x in bg_data]
        request_body = {
            'values': values
        }
        print(f'Preparing to send request to write {len(values)} rows.')
        try:
            result = self.__service.spreadsheets().values().append(
                spreadsheetId=self.SPREADSHEET_ID,
                range=self.DATA_DUMP_RANGE,
                valueInputOption=ValueInputOption.USER_ENTERED.value,
                body=request_body
            ).execute()
            print(f'Success! {result.get("updates").get("updatedRows")} rows have been updated.')
        except:
            print('ERROR while attempting to update spreadsheet')
            raise

    DATA_DUMP_RANGE = "A:G"

    # If modifying these scopes, delete the file token.json.
    SCOPES = [APIScope.SPREADSHEETS.value]

    SPREADSHEET_ID = '1uZx-LR6VPt8U_Zb1YM60qw8NwAgxFys4n1dk1VWKpao'
