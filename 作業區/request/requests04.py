import requests
from bs4 import BeautifulSoup

url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020"
html = requests.get(url).text
soup = BeautifulSoup(html)
titles = soup.find_all("img", {"class":"cover"})
for i, title in enumerate(titles):
	print("第{}名：{}".format(i+1, title['alt']))
