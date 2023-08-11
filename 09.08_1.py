import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
link = 'https://demoqa.com/alerts'
browser.get(link)
browser.maximize_window()

button = browser.find_element(By.XPATH, '//*[@id="timerAlertButton"]')
button.click()

alert_wait = WebDriverWait(browser, 6).until(
    EC.alert_is_present()
)
alert = browser.switch_to.alert
alert.accept()
time.sleep(3)
print('GOOD TEST')
