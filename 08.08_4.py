import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = 'https://www.provartesting.com/contact/?utm_source=google&utm_medium=cpc&utm_campaign=uk_competitor&gclid=Cj0KCQjwz8emBhDrARIsANNJjS5nGD0ripp8PE5713StPCS5Ay_rdYqVyo6yxC6-LmVHKhwc618lwqwaAoOeEALw_wcB'
browser = webdriver.Chrome()
browser.get(link)

dropdown = browser.find_element(By.XPATH, '//*[@id="input_11_10"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", dropdown)
dropdown = Select(dropdown)
dropdown.select_by_value('Russian Federation')

time.sleep(3)

