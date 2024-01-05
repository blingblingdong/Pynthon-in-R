# 寫一支python 將https://www.novel543.com/0214212665/8012_1.html所有放在class="chapter-content px-3"裡的p標籤
# 的內容讀取出來，並且印出來

from bs4 import BeautifulSoup
import requests
import time

def clean_filename(filename):
    # 移除或替换不合法的文件名字符
    filename = filename.replace('/', '-').replace('\\', '-').strip()
    # 您可以添加更多的替换规则来处理其他特殊字符
    return filename


def readparagraph(string):
    string = string.replace("。", "。\n")
    paragraphs = string.split("\n")
    cleaned_paragraphs = [p.strip() for p in paragraphs if p.strip()]
    return cleaned_paragraphs
  
def printlist(list, waitingtime):
    for item in list:
        print(item)
        time.sleep(waitingtime)

for i in range(1, 10):
    url = "https://www.novel543.com/0214212665/8012_" + str(i) + ".html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    story_div = soup.find("div", class_="chapter-content px-3")
    paragraphs = story_div.find_all("p") if story_div else []

    full_text = ''.join(paragraph.get_text() for paragraph in paragraphs)

    title = soup.find("h1")
    title_text = title.get_text() if title else f"Chapter_{i}"

    story_paragraphs = readparagraph(full_text)

    title_text = clean_filename(title_text)

    with open(f"story/{title_text}.txt", "w", encoding="utf-8") as f:
        for paragraph in story_paragraphs:
            f.write(paragraph + "\n")








import os
from pydub import AudioSegment

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
