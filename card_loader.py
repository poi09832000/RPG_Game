# card_loader.py
# -*- coding: utf-8 -*-
import pandas as pd

def load_all_cards():
    """
    這個函式負責讀取 Excel 檔案中所有的工作表。
    成功時，它會回傳所有卡片的 DataFrame。
    失敗時 (例如找不到檔案)，它會引發一個 FileNotFoundError。
    """
    
    file_path = '艾爾德隆卡牌登錄表V2.xlsx'
    
    print("正在讀取卡片資料庫...")
    
    # 讀取所有工作表
    hero_card = pd.read_excel(file_path, sheet_name='勇者卡')
    skill_card = pd.read_excel(file_path, sheet_name='技能卡')
    mana_card = pd.read_excel(file_path, sheet_name='憶值卡')
    equipment_card = pd.read_excel(file_path, sheet_name='裝備卡')
    tactics_card = pd.read_excel(file_path, sheet_name='戰術卡')
    keyword = pd.read_excel(file_path, sheet_name='關鍵字')
    status = pd.read_excel(file_path, sheet_name='狀態')
    
    print("資料庫讀取成功！")
    
    # 將所有讀取到的 DataFrame 一次全部回傳出去
    return hero_card, skill_card, mana_card, equipment_card, tactics_card, keyword, status