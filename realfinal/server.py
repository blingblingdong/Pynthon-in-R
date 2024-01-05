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



story_dict = {}


def read_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            input_file = os.path.join(folder_path, filename)
            with open(input_file, "r", encoding='utf-8') as f:
                  story_content = readparagraph(f.read())
            story_name = filename.replace(".txt", "")
            story_dict[story_name] = story_content
              
read_folder('story')

while True:
  tool = input("你是1.使用者？2.管理者？3.離開")
  
  if tool == "1":
    while True:
      print("歡迎來聽故事")
      speed = setspeed()
      
      for i in list(story_dict.keys()):
        print(f"{i}",end=" ")
      answer1 = input("請選擇故事: ")
      
      if speed == 6:
        pygame.mixer.init()
        for i, paragraph in enumerate(story_dict[answer1]):
          play_and_print(f"mp3/{answer1}{i}.mp3", paragraph)
          os.remove(f"mp3/{answer1}{i}.mp3")
      elif speed == 7:
        for i in story_dict[answer1]:
          print(i)
          input("")
      else:
        printlist(story_dict[answer1],speed)
      
      answer2 = input("還要聽嗎？(y/n)")
        
      if answer2 == "n":
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


