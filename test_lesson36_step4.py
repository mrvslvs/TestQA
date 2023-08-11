import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://stepik.org/lesson/236895/step/1"


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    time.sleep(3)
    browser.quit()


class TestMainPage1():
    @pytest.mark.smoke
    def test_1(self, browser):
        browser.get(link)

        button_login = browser.find_element(By.XPATH, '//*[@id="ember33"]')
        button_login.click()

        user_login = browser.find_element(By.XPATH, '//*[@id="id_login_email"]')
        user_login.send_keys('vasmariya@bk.ru')

        user_pass = browser.find_element(By.XPATH, '//*[@id="id_login_password"]')
        user_pass.send_keys('25071961')

        button = browser.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/button')
        button.click()
        time.sleep(3)




