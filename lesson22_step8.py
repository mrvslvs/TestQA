import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

first_name = browser.find_element(By.XPATH, '/html/body/div/form/div/input[1]')
first_name.send_keys('Ivan')

last_name = browser.find_element(By.XPATH, '/html/body/div/form/div/input[2]')
last_name.send_keys('Ivanov')

email = browser.find_element(By.XPATH, '/html/body/div/form/div/input[3]')
email.send_keys('ivan.ivanov@mail.ru')

add_file = browser.find_element(By.XPATH, '//*[@id="file"]')
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
add_file.send_keys(file_path)

button_submit = browser.find_element(By.XPATH, '/html/body/div/form/button')
button_submit.click()

# закрываем браузер после всех манипуляций
time.sleep(3)
browser.quit()