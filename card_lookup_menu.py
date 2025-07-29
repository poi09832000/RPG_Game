import pandas as pd
import time

def card_lookup_menu(hero_card_df):
    """卡片查詢功能的獨立選單"""
    # 將你原本的卡片查詢 while 迴圈完整搬到這裡
    while True:
        # 我們將傳入的 hero_card_df 用於查詢
        print("\n--- 卡片查詢系統 ---")
        heronum_input = input('請輸入勇者卡號 (或輸入 q 返回主選單): ')

        if heronum_input.lower() == 'q':
            print("正在返回主選單...")
            time.sleep(1)
            break # 使用 break 來跳出這個迴圈，就會回到主選單

        try:
            hero_index = int(heronum_input) - 1
        except ValueError:
            print("錯誤: 輸入無效，請輸入一個數字卡號。")
            print("-" * 30)
            continue

        if 0 <= hero_index < len(hero_card_df):
            try:
                hero_data = hero_card_df.iloc[hero_index]
                
                print("\n--- 勇者卡片資訊 ---")
                for column_name, value in zip(hero_card_df.columns, hero_data):
                    print(f"{column_name}: {value}")
                print("-" * 30)

            except Exception as e:
                print(f"讀取資料時發生未預期的錯誤: {e}")
                print("-" * 30)
        else:
            print()
            print("-" * 30)
            print(f"錯誤: 找不到卡號 {heronum_input}。有效範圍是 1 到 {len(hero_card_df)}。")
            print("-" * 30)