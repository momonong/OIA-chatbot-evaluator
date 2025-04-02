import pandas as pd
from datetime import datetime

def build_threads(df: pd.DataFrame, date_col='日期', question_col='問題', answer_col='回覆', user_col='使用者'):
    """
    將資料依使用者分群並依時間排序，建立 conversation + target_turn 格式。

    Returns:
        List of dicts: 每一筆包含完整對話與評估目標
    """
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df = df.sort_values(by=[user_col, date_col])

    results = []
    thread_id = 0

    for user, group in df.groupby(user_col):
        conversation = []
        for i, row in enumerate(group.itertuples()):
            # 每一筆資料都會被當成要評估的回合（使用者發言）
            conversation_so_far = []

            # 前面的發言
            for j in range(i + 1):
                conversation_so_far.append({"role": "user", "message": getattr(group.iloc[j], question_col)})
                conversation_so_far.append({"role": "assistant", "message": getattr(group.iloc[j], answer_col)})

            # 當前是第幾個使用者 turn（0-based）
            target_turn = i * 2  # 使用者的回合在偶數 index（0, 2, 4,...）

            results.append({
                "user": user,
                "datetime": getattr(row, date_col),
                "conversation": conversation_so_far,
                "target_turn": target_turn
            })

        thread_id += 1

    return results
