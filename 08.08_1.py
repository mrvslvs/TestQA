from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()

value_1 = browser.find_element(By.XPATH, '//*[@id="num1"]')
value_1 = value_1.text
value_2 = browser.find_element(By.XPATH, '//*[@id="num2"]')
value_2 = value_2.text
value_sum = int(value_1) + int(value_2)

dropdown = Select(browser.find_element(By.XPATH, '//*[@id="dropdown"]'))
dropdown.select_by_value(str(value_sum))

button = browser.find_element(By.XPATH, '/html/body/div/form/button')
button.click()
time.sleep(3)
browser.quit()
