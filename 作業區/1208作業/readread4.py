
# 先寫一個空list
list = []

# 寫一個函式，讀取一段文字，並以句點將每句開，放入一個list中

def readparagraph(string):
    string = string.replace("。", "。\n")
    paragraphs = string.split("\n")
    cleaned_paragraphs = [p.strip() for p in paragraphs if p.strip()]
    return cleaned_paragraphs

  
ex = readparagraph("我是一個好人。我是一個壞人。我是一個正常人。")

print(ex)

# 寫一個函式，將list以迴圈的形式將每一句話印出來

import time

def printlist(list,waitingtime):
    for i in list:
        print(i)
        time.sleep(waitingtime)
        
printlist(ex)

story1_1 = "那年的聖誕夜，在薩摩亞的一個古老村莊，我和一群當地孩子在教堂旁的墓地玩捉迷藏。夜幕低垂，陰影籠罩了這片古老的墓地，創造出一種詭異的氛圍。我們躲藏在墓碑間，月光透過教堂的破碎窗戶照射進來。"
story1_2 = "一名男孩誤以為他哥哥躲在了教堂內，於是孤身一人踏進了這座古老的建築。教堂內寂靜無聲，唯有他的腳步聲在空蕩的走廊中回響。當他靠近祭壇時，他驚恐地發現前方站著一個身影，背對著他，身體扭曲不自然。"
story1_3 = "他的哥哥站在那裡，他的臉色蒼白，雙眼緊閉，雙手緊握著一個小小的棺材。男孩嚇得尖叫起來，他的哥哥轉過身來，他的臉上滿是淚水。他哥哥說「死了、死了，我們都要死了」。"
story1_4 = "男孩驚恐地昏倒在地，當我們找到他時，他臉色蒼白，嘴裡喃喃自語著不祥的預言。從那天起，他就一直生病，說他能聽到那個幽靈的聲音在夜裡呢喃。村民們開始避開那座教堂，認為那裡有一個惡靈守護著。自那以後，每當聖誕夜降臨，教堂周圍總是籠罩著一層不可名狀的恐懼。"
story1_5 = "只有我們知道，男孩的靈魂，永遠地被困在了那座古老的教堂裡。"

story1 = readparagraph(story1_1 + story1_2 + story1_3 + story1_4 + story1_5 + string_representation)

story2_1 = "感謝大家耐心地觀看，最後我們兩要來分享一下心得。我在這節課學到了不少有關python的技術，有read_file，list...。"
story2_2 = "我覺得這些技術都很實用，我們可以用這些技術來做很多事情，像是讀取檔案，或是將一段文字分割成一個個句子。"
story2_3 = "比起以前，需要在一知半解的狀況下，這堂課老師將觀念講解十分清楚。助教也十分耐心解答我們各種基礎問題"
story2_4 = "在這堂課程中已給予了相當大的彈性，讓我們能彼此腦力激盪，做出意想不到的有趣作品。"

story2 = readparagraph(story2_1 + story2_2 + story2_3 + story2_4)

storylist = [story1,story2]

for i in storylist:
    printlist(i,5)
    print("\n")
    
# 客戶端
# 1選擇故事、2選擇速度(快板、慢板、念稿機版)
# 純文字版、圖片輔助版

# 伺服器端
# 將file讀取成list


read_file = open("story.txt","r",encoding="utf-8")
x = read_file.read()
story3 = readparagraph(x)
printlist(story3,0.5)

# 寫一支python 將https://www.novel543.com/0214212665/8012_1.html所有放在class="chapter-content px-3"裡的p標籤
# 的內容讀取出來，並且印出來

from bs4 import BeautifulSoup
import requests

url = "https://www.novel543.com/0214212665/8012_1.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

story = soup.find("div", class_="chapter-content px-3")
paragraphs = story.find_all("p")

# 提取每個<p>標籤的文本並合併它們
full_text = ''.join(paragraph.get_text() for paragraph in paragraphs)


print(full_text)

story3 = readparagraph(full_text)
printlist(story3,0.5)

# 將full_text存成txt檔案
with open("story.txt", "w", encoding="utf-8") as f:
    f.write(full_text)


# 在consle print gg.png

from PIL import Image



ghost = Image.open("duck.jpeg")

# 将图像转换为灰度
ghost = ghost.convert('L')

# 将图像转换为1位像素宽度，这会创建一个点子图（点阵图）效果
ghost_ponit = ghost.convert('1')

# 保存或显示转换后的图像
ghost_ponit.save("duck_ponit.jpeg")

# 打开并可能调整图像大小
image = Image.open("duck_ponit.jpeg")
resized_image = image.convert('L').resize((100, 100))  # 转换为灰度图并调整大小

# 获取图像尺寸
width, height = resized_image.size

# 创建字符串表示
string_representation = ""
for y in range(height):
    for x in range(width):
        pixel = resized_image.getpixel((x, y))
        string_representation += '█' if pixel < 128 else ' '  # 对于灰度图，我们将亮度小于128的像素视为“黑色”
    string_representation += '\n'

# 打印字符串表示的点阵图
print(string_representation)
story1 = readparagraph(story1_1 + story1_2 + story1_3 + story1_4 + story1_5 + string_representation)
printlist(story1,0.3)


from gtts import gTTS
import os

def text_to_speech(text, filename):
    tts = gTTS(text, lang='zh-cn')
    tts.save(filename)

# 假设 readparagraph 函数已正确定义并返回了段落列表
聖誕節鬼故事 = readparagraph(story1_1 + story1_2 + story1_3 + story1_4 + story1_5)

# 为每个段落生成一个音频文件
for i, paragraph in enumerate(聖誕節鬼故事):
    text_to_speech(paragraph, f"story_part{i}.mp3")

import pygame
import time

# 初始化pygame音频模块
pygame.mixer.init()

def play_and_print(filename, text):
    # 播放音频
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # 打印文本
    print(text)

    # 等待音频播放结束
    while pygame.mixer.music.get_busy():
        time.sleep(1)

# 为每个段落播放音频并打印文本
for i, paragraph in enumerate(聖誕節鬼故事):
    play_and_print(f"story_part{i}.mp3", paragraph)
    
# 寫一個自動將照片轉成點陣圖的程式

def image_to_ascii(original, width, height):
  image = Image.open(original)
  image = image.convert('L').resize((width, height))
  width, height = image.size
  string_representation = ""
  for y in range(height):
    for x in range(width):
      pixel = image.getpixel((x, y))
      string_representation += '█' if pixel < 128 else ' '
    string_representation += '\n'
    
    return string_representation

 

system('python3 sever.py')


def speed_up_audio(input_file, output_file, speed=1.2):
    audio = AudioSegment.from_file(input_file)
    fast_audio = audio.speedup(playback_speed=speed)
    fast_audio.export(output_file, format="mp3")

def process_folder(folder_path, speed=1.2):
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3"):
            input_file = os.path.join(folder_path, filename)
            output_file = os.path.join(folder_path, filename)
            speed_up_audio(input_file, output_file, speed)

process_folder('mp3')
