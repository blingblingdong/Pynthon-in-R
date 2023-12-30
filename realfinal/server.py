from gtts import gTTS
import os
import pygame
import time


def readparagraph(string):
    string = string.replace("。", "。\n")
    paragraphs = string.split("\n")
    cleaned_paragraphs = [p.strip() for p in paragraphs if p.strip()]
    return cleaned_paragraphs
  
def printlist(list,waitingtime):
    for i in list:
        print(i)
        time.sleep(waitingtime)
        
        
def text_to_speech(text, filename):
    tts = gTTS(text, lang='zh-cn')
    tts.save(filename)
    
def play_and_print(filename, text):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    print(text)

    while pygame.mixer.music.get_busy():
        time.sleep(1)
        
        
def setspeed():
  speed1 = input("請選擇速度：1快板、2慢板、3google小姐版、4手動版")
    
  if speed1 == "1":
    speed = 1
  elif speed1 == "2":
    speed = 5
  elif speed1 == "3":
    speed = 6
  elif speed1 == "4":
    speed = 7
    
  return speed

# 寫一個函式，讀取一段文字，並以句點將每句開，放入一個list中

story1_1 = "那年的聖誕夜，在薩摩亞的一個古老村莊，我和一群當地孩子在教堂旁的墓地玩捉迷藏。夜幕低垂，陰影籠罩了這片古老的墓地，創造出一種詭異的氛圍。我們躲藏在墓碑間，月光透過教堂的破碎窗戶照射進來。"
story1_2 = "一名男孩誤以為他哥哥躲在了教堂內，於是孤身一人踏進了這座古老的建築。教堂內寂靜無聲，唯有他的腳步聲在空蕩的走廊中回響。當他靠近祭壇時，他驚恐地發現前方站著一個身影，背對著他，身體扭曲不自然。"
story1_3 = "他的哥哥站在那裡，他的臉色蒼白，雙眼緊閉，雙手緊握著一個小小的棺材。男孩嚇得尖叫起來，他的哥哥轉過身來，他的臉上滿是淚水。他哥哥說「死了、死了，我們都要死了」。"
story1_4 = "男孩驚恐地昏倒在地，當我們找到他時，他臉色蒼白，嘴裡喃喃自語著不祥的預言。從那天起，他就一直生病，說他能聽到那個幽靈的聲音在夜裡呢喃。村民們開始避開那座教堂，認為那裡有一個惡靈守護著。自那以後，每當聖誕夜降臨，教堂周圍總是籠罩著一層不可名狀的恐懼。"
story1_5 = "只有我們知道，男孩的靈魂，永遠地被困在了那座古老的教堂裡。"

聖誕節鬼故事 = readparagraph(story1_1 + story1_2 + story1_3 + story1_4 + story1_5)

story2_1 = "感謝大家耐心地觀看，最後我們兩要來分享一下心得。我在這節課學到了不少有關python的技術，有read_file，list...。"
story2_2 = "我覺得這些技術都很實用，我們可以用這些技術來做很多事情，像是讀取檔案，或是將一段文字分割成一個個句子。"
story2_3 = "比起以前，需要在一知半解的狀況下，這堂課老師將觀念講解十分清楚。助教也十分耐心解答我們各種基礎問題"
story2_4 = "在這堂課程中已給予了相當大的彈性，讓我們能彼此腦力激盪，做出意想不到的有趣作品。"

suprise = readparagraph(story2_1 + story2_2 + story2_3 + story2_4)

story3_1t = "華人新年的習俗。"
story3_1 ="對我們中華人民來說，新年是富有重要意涵的喜慶時節，新年泛指從農曆年的除夕夜一直持續到正月十五（同時是社畜們的開工日）元宵節。這段期間充滿了各種傳統的習俗，讓人們歡聚一堂，共同迎接新的一年。首先是除夕夜的「團圓飯」，這是一個家庭聚餐的傳統活動，不論當下哪位家庭成員遠在他鄉，都會特別返鄉與家人共度美好時光、共享佳餚。此外，家家戶戶門外都會貼起春聯與對聯，祈求一年份的吉祥平安，也會黏貼各種吉祥的紅紙剪影，祈求好運與平安。到了夜晚會燃放煙花與爆竹，以驅趕邪靈，迎接新年的到來。而在正月初一，拜年是一項重要的習俗。長輩會給予晚輩紅包，象徵著祝福和好運。小孩們通常會拜訪親戚朋友，獲得長輩的祝福和紅包，這也是一種尊敬和孝順的表現。此外，人們還會去廟宇叩拜神明，祈求來年的平安和順遂。"
story3_2t = "與西方的異同。"
story3_2 ="東西兩方慶祝新年的方式有很大的差異。華人農曆計算日期，西方新年則是根據格里高利曆（陽曆）。兩邊都是1月1日卻足足差了一個多月。其次，我們華人慶祝活動的儀式更加搞工。在西方，人們主要通過跨年晚會、煙火和派對等方式慶祝新年，而在華人社會，新年的慶祝活動更加著重於家庭團聚、祭神拜祖、傳統舞龍舞獅等濃厚的文化元素。最後是小孩堅持過新年的重要信念，紅包。這是我們華人新年獨特的傳統，紅包是一種送禮的形式，代表著祝福和好運。在西方文化中並不常見。"
story3_3t = "新年的傳說。"
story3_3 ="華人新年的慶祝活動充滿了豐富的傳說，其中一個最為著名的就是「年獸」的故事。相傳在古代，有一頭凶惡的怪獸叫做年獸，它每到除夕夜就會出現，威脅著人們的生活。後來，人們發現年獸害怕紅色、煙火和響亮的聲音，於是開始在除夕夜掛紅對聯、燃放煙火，以及敲鑼打鼓，用這些方式驅趕年獸，保護家園。此外，舞龍舞獅也是新年慶祝活動中的獨特元素。相傳，舞龍舞獅可以驅逐邪靈，帶來好運和豐收。每逢新年，人們都會在街頭巷尾觀看精彩的舞獅表演，希望這種傳統藝術能為新的一年帶來吉祥和繁榮。總的來說，華人新年的習俗豐富多彩，蘊含著悠久的歷史和深厚的文化內涵。這個傳統節日不僅是一個家庭團聚的時刻，更是一個祈求吉祥、擁抱未來的重要時刻。在這個特別的日子裡，人們共同迎接新的一年，滿懷希望地迎接未來的挑戰。"

新年故事1 = readparagraph(story3_1t + story3_1)
新年故事2 = readparagraph(story3_2t + story3_2)
新年故事3 = readparagraph(story3_3t + story3_3)

新年故事 = 新年故事1 + 新年故事2 + 新年故事3


# 所有已經被readparagraph整理過的故事，都放在這裡
storylist = [聖誕節鬼故事] 

# 寫一個dictionary，讓使用者可以選擇故事

story_dict = {"聖誕節鬼故事":聖誕節鬼故事,"新年故事":新年故事}

# 我可以在pyton dictionary中加入新的key-value pair嗎？
# A:可以，用update


while True:
  tool = input("你是1.使用者？2.管理者？3.離開")
  
  if tool == "1":
    while True:
      print("安安你好，你幾歲啊？住哪？來聽故事？\n我手邊剛好有幾個故事？\n咳咳")
      speed = setspeed()
      
      for i in list(story_dict.keys()):
        print(f"{i}",end=" ")
      answer1 = input("請選擇故事: ")
      
      if speed == 6:
        pygame.mixer.init()
        for i, paragraph in enumerate(story_dict[answer1]):
          play_and_print(f"mp3/{paragraph}{i}.mp3", paragraph)
          os.remove(f"mp3/{paragraph}{i}.mp3")
      elif speed == 7:
        for i in story_dict[answer1]:
          print(i)
          input("")
      else:
        printlist(story_dict[answer1],speed)
      
      answer2 = input("還要聽嗎？(y/n)")
        
      if answer2 == "n":
        printlist(suprise,speed)
        break
  elif tool == "2":
    chose1 = input("今天是要：1.寫故事、2.管理故事")
    if chose1 == "1":
      while True:
          print("要用什麼形式來輸入故事呢？")
          choose = input("1.手動輸入故事 2.txt轉故事 3.轉語音 4.退出")
      
          if choose == "1":
              story_name = input("請輸入故事名稱，按空白鍵退出: ")
              story_content = []
              while True:
                  sentence = input("請輸入故事句子: ")
                  if sentence == "":
                      break
                  story_content.extend(readparagraph(sentence))
              story_dict[story_name] = story_content
      
          elif choose == "2":
              story_name = input("請輸入故事名: ")
              txt_name = input("請輸入txt檔名: ")
              with open(txt_name, "r", encoding='utf-8') as f:
                  story_content = readparagraph(f.read())
              story_dict[story_name] = story_content
      
          elif choose == "3":
              story_name = input("請輸入故事名: ")
              if story_name in story_dict:
                  for i, paragraph in enumerate(story_dict[story_name]):
                      text_to_speech(paragraph, f"mp3/{story_name}{i}.mp3")
              else:
                  print("故事名稱不存在。")
      
          elif choose == "4":
              break
          else:
              print("無效的選項，請重新輸入。")
    elif chose1 == "2":
      while True:
        print("故事列表: ")
        for name in story_dict.keys():
          print(name)
        s_name = input("請輸入想處理故事名稱")
        s_input = input("要怎麼處理故事呢？1.確認故事、2.刪除故事、3.寫出故事(text)、4.退出")
        if s_input == "1":
          printlist(story_dict[s_name],0.2)
        elif s_input == "2":
           if s_name in story_dict:
              del story_dict[s_name]
        elif s_input == "3":
          with open(f"story/{s_name}.txt","w",encoding="utf-8") as f:
            for i in story_dict[s_name]:
              f.write(i)
            print("寫出成功!")
        elif s_input == "4":
          break
        
  elif tool == "3":
    print("掰掰")
    break


