def set():
    global name
    global x
    answer = 3
    while True:
        if answer == 1:
            break
        else:
            x = int(input("輸入生命值： "))
            name = str(input("輸入名字："))
            print(f"你要叫做{name}，並且有{x}條生命嗎？")
            answer = int(input("是輸入1，重新設定輸入2:"))


def 關卡set():
  global name
  global 關卡
  關卡 = 0
  answer = 0

  print(f"pov：{name}，請選擇你的關卡")
  print("pov：建議您，循序漸進...")
  關卡 = int(input("選擇你的關卡\n1：基礎題、2：進階題、3：魔王題："))
      


def attack(a):
    global x
    x = x - a
    print(f"你只剩下{x}機會了")

def 關卡1(答案, 問題, 問題選項, 解釋,提示):
    global x
    while x > 0:
        if x <= 0:
            print("你沒命囉")
            break

        answer = input(f"{問題}\n{問題選項}：")
        
        if answer == 答案:
            print(解釋)
            break

        attack(1)
        print(f"提示：{提示}")
        
        
        
def 關卡2(答案, 問題, 問題選項, 解釋,提示):
    global x
    while x > 0:
        if x <= 0:
            print("你沒命囉")
            break

        answer = input(f"{問題}\n{問題選項}：")
        
        if answer == 答案:
            print(解釋)
            break

        attack(2)
        print(f"提示：{提示}")
        
        
def 關卡3(答案, 問題, 問題選項, 解釋,提示):
    global x
    while x>0:
        if x <= 0:
            print("你沒命囉")
            break

        answer = input(f"{問題}\n{問題選項}：")
        
        if answer == 答案:
            print(解釋)
            break

        attack(3)
        print(f"提示：{提示}")
        
        
        
        
        
def 關卡reset():
  global flag
  global 關卡
  if 關卡 == 1:
    print("巫婆：矮油不錯呦")
    print("pov：巫婆開始覬覦你的肉體...")
  elif 關卡 == 2:
    print("巫婆：可惡!")
    print("巫婆：魔鏡、魔鏡，誰是世界上最美麗的女人")
    print("pov：此時巫婆已經歇斯底里...")
    print("pov：噠啦噠啦")
    print("魔鏡：噠啦噠啦")
    print("魔鏡：美麗島?")
    print("巫婆：恩？")
    print("pov：此時巫婆恍然發現你已通過第二關")
  elif 關卡 == 3:
    print("pov：巫婆使用耍賴技能")
    print(f"pov：此時{name}發現食人🌲已釋放了他，迷霧卻未散去")
    input(f"pov：是否發動冷笑話激光？ ")
    print(f"{name}：哈利波特裡面誰最有主見?")
    print("魔鏡：佛地魔？")
    print("pov：請打倒魔鏡!")
    print(f"{name}：如果吳宗憲是NBA當年度的MVP，進攻得分像切菜一樣輕快，應該找誰來防守他")
    print("魔鏡：誒誒誒...")
    print("魔鏡：...")
    print("魔鏡：...")
    print("魔鏡：...")
    input("pov：按下f鍵使用車窗擊破器! ")
    print("魔鏡：慈母守宗憲!")
    print("碰！")
    print("pov：魔鏡受到致命物理傷害!")
    print("pov：迷霧散去，再見了！可魯")
    print(f"{name}：原來我是狗")
    print("pov：沒有你連狗都不如")
    print(f"{name}ㄍㄢ..")
    print("pov：正在進行回溯...")
  flag = int(input("挑戰別的關卡?\n3：yes，2：no"))


