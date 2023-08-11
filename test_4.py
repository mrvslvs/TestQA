import datetime
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'http://saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print('Input Login')
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print('Input Password')
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print('Click Login button')
# text_products = driver.find_element(By.XPATH, "//span[@class='title']")
# value_text_products = text_products.text
# print(value_text_products)
#
# assert value_text_products == 'Products'
# print('GOOD')

# url = 'https://www.saucedemo.com/inventory.html'
# get_url = driver.current_url
# print(get_url)
# assert url == get_url
# print('Good URL')



# driver.execute_script('window.scrollTo(0, 200)')
action = ActionChains(driver)
red_t_shirt = driver.find_element(By.XPATH, '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
action.move_to_element(red_t_shirt).perform()

time.sleep(5)

now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot("C:\\Users\\055\\PycharmProjects\\TIS_05\\" + name_screenshot)



time.sleep(3)
driver.quit()