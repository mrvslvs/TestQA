import math
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)

button_1 = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
button_1.click()

confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = x_element.text
y = calc(x)

answer = browser.find_element(By.XPATH, '//*[@id="answer"]')
answer.send_keys(y)

button_submit = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
button_submit.click()

# закрываем браузер после всех манипуляций
time.sleep(3)
browser.quit()