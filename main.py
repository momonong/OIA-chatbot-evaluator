from config import SheetConfig
from tabulate import tabulate
from clients.sheet_client import init_google_sheet
from functions.sheet_utils import load_sheet_data
from functions.thread_builder import build_threads
from functions.io_utils import save_json_with_date
import json

def main():
    config = SheetConfig()

    worksheet = init_google_sheet(
        service_account_path=config.SERVICE_ACCOUNT_PATH,
        spreadsheet_id=config.GOOGLE_SHEET_ID,
        sheet_name="filtered_loglists"
    )

    df = load_sheet_data(worksheet)

    preview_df = df[['日期', '問題', '回覆']].head(5)
    print(f"✅ 共讀取 {len(df)} 筆資料（來自 QUERY 結果）")
    print(tabulate(preview_df, headers='keys', tablefmt='grid'))

    threads = build_threads(df)

    # 儲存輸入資料
    save_json_with_date(threads, prefix="evaluation_input")

    # 預覽第一筆
    print("\n🧪 第一筆輸入：")
    from functions.io_utils import json_serial

    print(json.dumps(threads[0], indent=2, ensure_ascii=False, default=json_serial))

if __name__ == "__main__":
    main()
