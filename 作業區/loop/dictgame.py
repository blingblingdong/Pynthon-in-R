import random

# 卡牌資訊
cards = {
    "青眼白龍": 20,
    "紅髮女妖": 11,
    "白骷體王": 9,
    "碧眼狐怪": 12
}

# 魔王血量
boss_hp = 100

# 玩家卡牌，初始時可能只有一部分卡牌
player_cards = ["青眼白龍", "碧眼狐怪"]

def attack_boss():
    global boss_hp
    if player_cards:
        card = random.choice(player_cards)
        damage = cards[card]
        boss_hp -= damage
        print(f"使用 {card} 攻擊 {damage} 點，魔王目前血量：{boss_hp}")
    else:
        print("沒有卡牌可以攻擊！")

def replenish_cards():
    global player_cards
    player_cards = list(cards.keys())
    print("完成補齊卡牌！")

def show_cards():
    print("目前卡牌：", ", ".join(f'"{card}": {cards[card]}' for card in player_cards))

while boss_hp > 0:
    print("\n功能選項：1.抽卡攻擊 2.補齊卡牌 3.目前卡牌 4.離開遊戲")
    choice = input("請輸入選項：")

    if choice == '1':
        attack_boss()
    elif choice == '2':
        replenish_cards()
    elif choice == '3':
        show_cards()
    elif choice == '4':
        print("退出遊戲。")
        break
    else:
        print("無效的選項。")

    if boss_hp <= 0:
        print("恭喜！你擊敗了魔王！")

# 檢查是否魔王血量已經歸零
if boss_hp <= 0:
    print("遊戲結束，你贏了！")
else:
    print("遊戲結束。")
