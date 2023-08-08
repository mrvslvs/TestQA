import math
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'https://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()

value = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = value.text
y = calc(x)

answer = browser.find_element(By.XPATH, '//*[@id="answer"]')
answer.send_keys(y)

checkbox = browser.find_element(By.XPATH, '/html/body/div/form/div[2]/label')
checkbox.click()

radiobutton = browser.find_element(By.XPATH, '/html/body/div/form/div[4]/label')
browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
radiobutton.click()

button_submit = browser.find_element(By.XPATH, '/html/body/div/form/button')
button_submit.click()

time.sleep(3)
browser.quit()
