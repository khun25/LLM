# 네이버 웹툰 댓글 크롤링
# https://comic.naver.com/webtoon/detail?titleId=834886&no=53&week=mon
import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://comic.naver.com/webtoon/detail?titleId=834886&no=53&week=mon')
soup = BeautifulSoup(driver.page_source)
comment_area = soup.find_all('span', {'class': 'u_cbox_contents'})
print('********** 베스트 댓글 **********')
for i in range(len(comment_area)):
    comment = comment_area[i].text.strip()
    print(comment)
    print('-' * 30)

time.sleep(10)