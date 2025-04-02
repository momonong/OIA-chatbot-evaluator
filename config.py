import os
from dotenv import load_dotenv

load_dotenv()

class SheetConfig:
    def __init__(self):
        self.GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
        self.SERVICE_ACCOUNT_PATH = os.getenv("SERVICE_ACCOUNT_PATH")
        self.SHEET_NAME = "loglists"