import requests

# 指定圖片網址
img_url='http://www.gotop.com.tw/Waweb2004/WawebImages/BookXL/AEL022200.jpg'
response= requests.get(img_url) 
# 指定開啟檔案路徑
# f=open('D:\\bootstrap.jpg','wb')  # on Windows
f=open('bootstrap.jpg','wb')
# 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
f.write(response.content)  			
print('下載完畢')
f.close()
