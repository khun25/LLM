# Samsung Stock Price from Toss
# https://tossinvest.com/stocks/A005930/order

import schedule
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument('headless')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://tossinvest.com/stocks/A005930/order')

time.sleep(3)

def job():
    str_time = time.strftime('%Y.%m.%d - %H:%M:%S')
    soup = BeautifulSoup(driver.page_source)
    spa = soup.find_all('div', {'class': 'njzdl31'})
    #print(type(spa))
    #print('\n\n\n')

    spl = [s.text for s in spa]
    #print(spl[0])
    #print('\n\n\n')

    spl = spl[0].strip().split(' ')
    #print(spl)

    spl = spl[1].strip().split('원')
    if int(spl[0].replace(',', '')) < 60000:
        print(f'{str_time} : {spl[0]}')
    else:
        print(f'{str_time} : {spl[0]} :: Sell?')

    time.sleep(3)

# schedule.every(1).minutes.do(job)
schedule.every(15).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
