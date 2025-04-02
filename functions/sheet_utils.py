import pandas as pd

def load_sheet_data(worksheet) -> pd.DataFrame:
    """
    從 worksheet 讀取資料轉為 pandas DataFrame（假設已在 Google Sheet 中 QUERY 過濾過）。
    """
    values = worksheet.get_all_values()
    df = pd.DataFrame(values[1:], columns=values[0])
    return df
