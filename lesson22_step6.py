from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.XPATH, '//input[@id="answer"]')
    answer.send_keys(y)

    check_box = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    check_box.click()

    radio_button = browser.find_element(By.XPATH, '/html/body/div/form/div[4]/label')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)
    radio_button.click()

    button_submit = browser.find_element(By.XPATH, '/html/body/div/form/button')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button_submit)
    button_submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
