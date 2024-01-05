import requests

url="https://www.books.com.tw/web/sys_saletopb/books/19/?loc=p_0002_020"
html=requests.get(url).text
keyword=input("請問你要查詢的字串(end to quit):")
while keyword!='end':
    print("{}這個字在排行榜中裡面出現了{}次".format(keyword, html.count(keyword)))
    keyword=input("請問你要查詢的字串(end to quit):")
