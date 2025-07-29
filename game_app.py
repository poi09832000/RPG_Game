import pygame
import sys
import os
import card_loader  # 導入你的卡牌讀取模組

# ======================================================================
# 1. 遊戲設定與初始化
# ======================================================================
pygame.init()

# --- 常數設定 ---
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
WINDOW_TITLE = "艾爾德隆傳說"
FPS = 60

# --- 顏色定義 ---
COLOR_BG = (245, 245, 220)
COLOR_TEXT = (0, 0, 0)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (150, 150, 150)
COLOR_LIGHT_GRAY = (200, 200, 200)
COLOR_BLUE = (100, 150, 220)
COLOR_INPUT_ACTIVE = (150, 200, 255)
COLOR_RED = (220, 100, 100)

# --- 建立視窗與時鐘 ---
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)
clock = pygame.time.Clock()

# --- 載入資源 ---
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    FONT_PATH = os.path.join(script_dir, "NotoSansTC-Regular.ttf")
    font_title = pygame.font.Font(FONT_PATH, 60)
    font_button = pygame.font.Font(FONT_PATH, 40)
    font_text = pygame.font.Font(FONT_PATH, 24)
    font_info = pygame.font.Font(FONT_PATH, 20)
    
    print("正在讀取卡牌資料庫...")
    (hero_card, skill_card, mana_card, equipment_card, 
    tactics_card, keyword, status) = card_loader.load_all_cards()
    print("資料庫讀取成功！")

except Exception as e:
    print(f"錯誤：資源載入失敗 - {e}")
    pygame.quit()
    sys.exit()

# ======================================================================
# 2. 遊戲狀態與場景管理
# ======================================================================
current_scene = "main_menu"

# --- 卡片查詢場景的變數 ---
input_box = pygame.Rect(SCREEN_WIDTH / 2 - 150, 150, 300, 50)
search_button = pygame.Rect(SCREEN_WIDTH / 2 - 75, 220, 150, 50)
back_button = pygame.Rect(30, 30, 100, 40)
input_text = ''
input_active = False
search_result_text = []

# ======================================================================
# 3. 繪製與邏輯函式
# ======================================================================

def draw_text(text, font, color, surface, x, y, center=False):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)
    return text_rect

def perform_search():
    """執行搜尋的邏輯，將結果存到全域變數中"""
    global search_result_text
    try:
        if not input_text:
            search_result_text = ["請先輸入卡號。"]
            return
            
        hero_index = int(input_text) - 1
        if 0 <= hero_index < len(hero_card):
            hero_data = hero_card.iloc[hero_index]
            search_result_text = []
            for col, val in zip(hero_card.columns, hero_data):
                search_result_text.append(f"{col}: {val}")
        else:
            search_result_text = [f"錯誤: 找不到卡號 {input_text}。", f"有效範圍是 1 到 {len(hero_card)}。"]
    except ValueError:
        search_result_text = ["錯誤: 輸入無效，請輸入一個數字卡號。"]
    except Exception as e:
        search_result_text = [f"發生未預期錯誤: {e}"]

# ... (draw_main_menu 和 draw_game_board 函式保持不變) ...
def draw_main_menu():
    screen.fill(COLOR_BG)
    draw_text("艾爾德隆傳說", font_title, COLOR_BLACK, screen, SCREEN_WIDTH / 2, 150, center=True)
    btn_start = draw_text("開始遊戲", font_button, COLOR_BLACK, screen, SCREEN_WIDTH / 2, 350, center=True)
    btn_lookup = draw_text("卡片查詢", font_button, COLOR_BLACK, screen, SCREEN_WIDTH / 2, 450, center=True)
    btn_quit = draw_text("結束程式", font_button, COLOR_BLACK, screen, SCREEN_WIDTH / 2, 550, center=True)
    return {"start": btn_start, "lookup": btn_lookup, "quit": btn_quit}

def draw_card_lookup():
    screen.fill(COLOR_BG)
    draw_text("卡片查詢系統", font_title, COLOR_BLACK, screen, SCREEN_WIDTH / 2, 80, center=True)

    # 按鈕上的文字維持白色，以確保在深色按鈕上的可讀性
    pygame.draw.rect(screen, COLOR_GRAY, back_button, border_radius=10)
    draw_text("返回", font_text, COLOR_WHITE, screen, back_button.centerx, back_button.centery, center=True)

    # 輸入框內的文字改為黑色
    color = COLOR_INPUT_ACTIVE if input_active else COLOR_GRAY
    pygame.draw.rect(screen, color, input_box, 2, border_radius=10)
    draw_text(input_text, font_button, COLOR_BLACK, screen, input_box.x + 15, input_box.centery - 20)
    
    # 搜尋按鈕文字維持白色
    pygame.draw.rect(screen, COLOR_BLUE, search_button, border_radius=10)
    draw_text("搜尋", font_button, COLOR_WHITE, screen, search_button.centerx, search_button.centery, center=True)
    
    # 結果區塊因為有自己的深色底色，所以裡面的文字維持白色
    if search_result_text:
        result_area = pygame.Rect(100, 300, SCREEN_WIDTH - 200, SCREEN_HEIGHT - 350)
        pygame.draw.rect(screen, (30,40,50), result_area, border_radius=10)
        y_offset = 320
        for line in search_result_text:
            draw_text(line, font_info, COLOR_WHITE, screen, 120, y_offset)
            y_offset += 30

def draw_game_board():
    screen.fill(COLOR_BG)
    # 按鈕文字維持白色
    pygame.draw.rect(screen, COLOR_GRAY, back_button, border_radius=10)
    draw_text("返回", font_text, COLOR_WHITE, screen, back_button.centerx, back_button.centery, center=True)
    
    # 標題和標籤文字改為黑色
    draw_text("遊戲場地 (開發中)", font_title, COLOR_BLACK, screen, SCREEN_WIDTH / 2, 80, center=True)
    
    slot_width, slot_height = 100, 140
    slot_color = (190, 190, 170) # 將卡槽顏色也調亮一些
    
    def draw_slots(y_pos, label):
        draw_text(label, font_text, COLOR_BLACK, screen, 80, y_pos + slot_height/2 - 12, center=True)
        for i in range(5):
            pygame.draw.rect(screen, slot_color, (150 + i * 120, y_pos, slot_width, slot_height), border_radius=10)
            
    draw_text("【對手區域】", font_text, COLOR_BLACK, screen, SCREEN_WIDTH/2, 150, center=True)
    draw_slots(180, "後場")
    draw_slots(330, "前場")
    
    draw_text("【我方區域】", font_text, COLOR_BLACK, screen, SCREEN_WIDTH/2, 490, center=True)
    draw_slots(520, "前場")
    draw_slots(670, "後場") # Y 座標調整為 670

# ======================================================================
# 4. 遊戲主迴圈
# ======================================================================
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # --- 通用事件 ---
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        
        # --- 主選單的事件處理 ---
        if current_scene == "main_menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons = draw_main_menu()
                if buttons["start"].collidepoint(mouse_pos):
                    current_scene = "game_board"
                elif buttons["lookup"].collidepoint(mouse_pos):
                    current_scene = "card_lookup"
                elif buttons["quit"].collidepoint(mouse_pos):
                    running = False

        # --- 卡片查詢的事件處理 (已修改) ---
        elif current_scene == "card_lookup":
            # 處理滑鼠點擊
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(mouse_pos):
                    current_scene = "main_menu"
                    input_text = ''
                    search_result_text = []
                    pygame.key.stop_text_input() # 離開時停用文字輸入
                elif search_button.collidepoint(mouse_pos):
                    perform_search()
                
                # --- 修改 1: 啟用/停用文字輸入 ---
                if input_box.collidepoint(mouse_pos):
                    input_active = True
                    pygame.key.start_text_input() # 告訴系統要開始接收輸入法文字
                    pygame.key.set_text_input_rect(input_box) # 設定輸入法視窗位置
                else:
                    input_active = False
                    pygame.key.stop_text_input() # 點擊其他地方時，停用文字輸入

            # --- 修改 2: 處理 TEXTINPUT 事件 (接收中文/英文) ---
            if event.type == pygame.TEXTINPUT and input_active:
                input_text += event.text

            # --- 修改 3: 更新 KEYDOWN 事件 (只處理功能鍵) ---
            if event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    perform_search()

        # --- 遊戲場地的事件處理 ---
        elif current_scene == "game_board":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(mouse_pos):
                    current_scene = "main_menu"

    # (B) 畫面繪製
    if current_scene == "main_menu":
        draw_main_menu()
    elif current_scene == "card_lookup":
        draw_card_lookup()
    elif current_scene == "game_board":
        draw_game_board()

    # (C) 更新畫面
    pygame.display.flip()
    clock.tick(FPS)

# ======================================================================
# 5. 結束程式
# ======================================================================
pygame.quit()
sys.exit()