import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://www.saucedemo.com/"


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


class TestMainPage1():
    @pytest.mark.smoke
    def test_1(self, browser):
        browser.get(link)

        user_login = browser.find_element(By.XPATH, '//*[@id="user-name"]')
        user_login.send_keys('standard_user')

        user_pass = browser.find_element(By.XPATH, '//*[@id="password"]')
        user_pass.send_keys('secret_sauce')

        button = browser.find_element(By.XPATH, '//*[@id="login-button"]')
        button.click()
        time.sleep(3)


    @pytest.mark.xfail
    def test_2(self, browser):
        browser.get(link)

        user_login = browser.find_element(By.XPATH, '//*[@id="user-name"]')
        user_login.send_keys('locked_out_user')

        user_pass = browser.find_element(By.XPATH, '//*[@id="password"]')
        user_pass.send_keys('secret_sauce')

        button = browser.find_element(By.XPATH, '//*[@id="login-button"]')
        button.click()
        time.sleep(3)

    def test_3(self, browser):
        browser.get(link)

        user_login = browser.find_element(By.XPATH, '//*[@id="user-name"]')
        user_login.send_keys('problem_user')

        user_pass = browser.find_element(By.XPATH, '//*[@id="password"]')
        user_pass.send_keys('secret_sauce')

        button = browser.find_element(By.XPATH, '//*[@id="login-button"]')
        button.click()
        time.sleep(3)

    def test_4(self, browser):
        browser.get(link)

        user_login = browser.find_element(By.XPATH, '//*[@id="user-name"]')
        user_login.send_keys('performance_glitch_user')

        user_pass = browser.find_element(By.XPATH, '//*[@id="password"]')
        user_pass.send_keys('secret_sauce')

        button = browser.find_element(By.XPATH, '//*[@id="login-button"]')
        button.click()
        time.sleep(3)