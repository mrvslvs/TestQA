import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = 'http://suninjuly.github.io/selects2.html'
browser = webdriver.Chrome()
browser.get(link)

first_number = browser.find_element(By.XPATH, '//*[@id="num1"]')
first_number = first_number.text
second_number = browser.find_element(By.XPATH, '//*[@id="num2"]')
second_number = second_number.text
summary = int(first_number) + int(second_number)
dropdown = browser.find_element(By.XPATH, '//*[@id="dropdown"]')
select = Select(dropdown)
select.select_by_value(str(summary))

button = browser.find_element(By.XPATH, '/html/body/div/form/button')
button.click()

# закрываем браузер после всех манипуляций
time.sleep(3)
browser.quit()