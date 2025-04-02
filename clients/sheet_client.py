import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

def init_google_sheet(service_account_path: str, spreadsheet_id: str, sheet_name: str):
    """
    初始化 Google Sheet 並回傳 worksheet。
    """
    scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    creds = Credentials.from_service_account_file(service_account_path, scopes=scopes)
    client = gspread.authorize(creds)
    worksheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
    return worksheet
