from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com')
search = driver.find_element('name', 'q')
search.send_keys('날씨')
search.send_keys(Keys.RETURN)

time.sleep(60)