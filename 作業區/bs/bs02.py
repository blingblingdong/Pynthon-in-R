from bs4 import BeautifulSoup

html = '''
<html>
    <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
    <body>
        <p id="p1">我是段落一</p>
        <p id="p2" class='red'>我是段落二</p>
    </body>
</html>
'''

bs=BeautifulSoup(html, "html.parser")

print(bs.find('p'))
print(bs.find_all('p'))            	
print(bs.find('p',{'id':'p2', 'class':'red'}))
print(bs.find('p',id='p2', class_='red'))
