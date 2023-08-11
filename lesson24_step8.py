from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

button1 = browser.find_element(By.XPATH, '//*[@id="book"]')
b = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

button1.click()
time.sleep(2)

x = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = int(x.text)
y = calc(x)

input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
input1.send_keys(y)

button2 = browser.find_element(By.XPATH, '//*[@id="solve"]')
button2.click()

time.sleep(3)
browser.quit()