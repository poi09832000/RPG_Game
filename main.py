# main.py

# 導入 Python 內建模組
import time

# 導入我們自己建立的模組
import card_loader
from card_lookup_menu import card_lookup_menu
from game_board import display_board  # <--- 新增這一行！

# ======================================================================
# 函式定義區 (現在變得非常乾淨！)
# ======================================================================

def start_game():
    """開始遊戲的函式，現在只負責呼叫顯示場地的功能"""
    display_board()  # 直接呼叫從外部導入的函式
    input("\n遊戲場地已建立。按下 Enter 返回主選單...")
    time.sleep(1)

# 注意：這裡已經不需要 display_board 和 card_lookup_menu 的函式定義了！

# ======================================================================
# 主程式進入點 (Main Program Execution)
# ======================================================================

if __name__ == "__main__":
    
    # 1. 程式啟動時，先讀取資料
    try:
        (hero_card, skill_card, mana_card, equipment_card, 
        tactics_card, keyword, status) = card_loader.load_all_cards()
    except FileNotFoundError:
        print(f"錯誤: 找不到卡片資料庫檔案 '艾爾德隆卡牌登錄表V2.xlsx'，請確認檔案位置是否正確。")
        exit()
    except Exception as e:
        print(f"讀取檔案時發生未預期的錯誤: {e}")
        exit()

    # 2. 進入主選單的無限迴圈
    while True:
        print("\n\n===== 艾爾德隆傳說 主選單 =====")
        print("      1. 開始遊戲")
        print("      2. 卡片查詢")
        print("      3. 結束程式")
        print("==============================")
        
        choice = input("請輸入您的選擇 (1-3): ")

        if choice == '1':
            start_game()
        
        elif choice == '2':
            card_lookup_menu(hero_card)
        
        elif choice == '3':
            print("感謝您的遊玩，程式已關閉。")
            break
        
        else:
            print("無效的輸入，請輸入 1, 2, 或 3。")
            time.sleep(1)