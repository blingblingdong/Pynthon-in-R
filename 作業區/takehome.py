import requests
from bs4 import BeautifulSoup

def fetch_super_lotto_results(url):
    # 發送HTTP請求到網頁
    response = requests.get(url)
    # 如果請求成功
    if response.ok:
        # 使用BeautifulSoup來解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        # 尋找包含開獎號碼的HTML元素，以下的類別名稱和標籤可能需要根據實際網頁結構進行調整
        draw_elements = soup.find_all('div', class_='draw_element_class_name')
        for draw in draw_elements:
            # 擷取和打印開獎日期和號碼
            date = draw.find('span', class_='date_class_name').text
            numbers = draw.find('span', class_='numbers_class_name').text
            print(f"Draw Date: {date}, Winning Numbers: {numbers}")
    else:
        print("Failed to retrieve the results.")

# 威力彩歷史開獎結果的網址
url = 'https://en.lottolyzer.com/history/taiwan/super-lotto-638/page/1/per-page/50/summary-view'
fetch_super_lotto_results(url)
