from selenium.webdriver.common.by import By
from selenium import webdriver
import time

link = 'https://ciricc.github.io/'
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()

element = browser.find_element(By.XPATH, '//*[@id="main-content"]/div/ul[1]/li[5]/a[2]')
element.click()
time.sleep(10)

element_find = browser.find_element(By.XPATH, '//*[@id="main-content"]/h1/text()')
element_find = element_find.text
assert element_find == 'Streaming API'
print('GOOD TEST')
