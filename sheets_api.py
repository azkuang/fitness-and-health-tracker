import os
from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build

#Gets variables from env file
load_dotenv()

SERVICE_ACCOUNT_FILE = "Credentials/fitness-and-health-tracker-26d478857f1d.json"

SPREADSHEET_ID = '1GU7neeq2JsYgcSy6oP5LS60-dDdLDE_nz6ih8cSQuQ0'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

class SheetsAPI:
    def __init__(self):
        self.creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        self.service = build('sheets', 'v4', credentials=self.creds)
        self.sheet = self.service.spreadsheets()

    def read_sheet(self, range_name):
        """Reads data from a range and returns it."""
        try:
            result = self.sheet.values().get(spreadsheetId=SPREADSHEET_ID, 
                                             range=range_name).execute()
            values = result.get('values', [])
            return values
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def write_to_sheet(self, range_name, values):
        """Writes data to a range."""
        try:
            body = {'values': values}
            result = self.sheet.values().update(
                spreadsheetId=SPREADSHEET_ID, range=range_name,
                valueInputOption='USER_ENTERED', body=body).execute()
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            return None