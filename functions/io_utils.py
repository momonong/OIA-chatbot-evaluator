import json
from pathlib import Path
from datetime import datetime
import pandas as pd

def json_serial(obj):
    """支援 pandas Timestamp 等 datetime 物件的序列化"""
    if isinstance(obj, (datetime, pd.Timestamp)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

def save_json_with_date(data, prefix="evaluation_input", folder="data"):
    date_str = datetime.now().strftime("%Y%m%d")
    filename = f"{prefix}_{date_str}.json"
    path = Path(folder) / filename

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=json_serial)

    print(f"📝 檔案已儲存：{path}")
