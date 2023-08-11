import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
button.click()

x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = x_element.text
y = calc(x)

time.sleep(3)
browser.quit()