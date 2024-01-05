from bs4 import BeautifulSoup
import requests

url='http://e-happy.com.tw/bsdemo1.htm' 
response=requests.get(url)

# 設定編碼模式避免亂碼
response.encoding = 'utf-8'

#傳回bs物件可解析網頁
bs=BeautifulSoup(response.text,"html.parser")
#bs=BeautifulSoup(response.text,"lxml")

#傳回網頁含<title>~</title>
print(bs.find('title'))

#傳回網頁<title>標籤內的資料
print(bs.find('title').text)

#傳回第一個符合<h1>資料
print(bs.find('h1'))
#若傳回None表示該網頁沒有<h1>標籤
