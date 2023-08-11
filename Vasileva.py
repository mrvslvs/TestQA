from telnetlib import EC

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


link = 'https://yohoho.cc/'
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()

search = browser.find_element(By.XPATH, '//*[@id="search-title"]')
search.send_keys('Драйв')
time.sleep(3)

button = browser.find_element(By.XPATH, '//*[@id="search"]')
button.click()
time.sleep(3)

element = browser.find_element(By.XPATH, '//*[@id="donate"]/div')
element = element.text

assert element == 'Просмотр доступен после доната любой суммы:'
print('GOOD TEST')

