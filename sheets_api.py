import os
from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build

#Gets variables from env file
load_dotenv()

SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Load credentials
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Initialize the Sheets API
service = build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()