# game_board.py

def display_board():
    """
    顯示遊戲主畫面的函式。
    使用文字和符號來描繪遊戲的各個區域。
    """
    # 為了讓畫面更乾淨，可以先清空舊畫面 (此功能在某些終端可能無效)
    # import os
    # os.system('cls' if os.name == 'nt' else 'clear')

    print("=" * 80)
    print("【對手區域】")
    print(f"後場: [      ] [      ] [      ] [      ] [      ]")
    print(f"前場: [      ] [      ] [      ] [      ] [      ]")
    print("-" * 80)
    print(" " * 60 + "對手手牌: [ 5 ]")
    print(" " * 60 + "對手憶值: [ 0 ]")
    print("\n" + "-" * 80)
    print(" " * 60 + "我方憶值: [ 0 ]")
    print(" " * 60 + "我方手牌: [ 5 ]")
    print("-" * 80)
    print("【我方區域】")
    print(f"前場: [      ] [      ] [      ] [      ] [      ]")
    print(f"後場: [      ] [      ] [      ] [      ] [      ]")
    print("=" * 80)
    print(f"| 牌組區: [ 45 ] | 棄牌區: [ 0 ] | 憶值區: [ 0 ] |")
    print("=" * 80)
    print("【我方手牌】")
    print("1: [空]  2: [空]  3: [空]  4: [空]  5: [空]")
    print("-" * 80)