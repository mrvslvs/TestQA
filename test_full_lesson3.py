import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://www.saucedemo.com/'


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    browser.get(link)
    yield
    browser.quit()


class TestMainPage1():
    @pytest.mark.xfail
    def test_locked_out(self, browser):


        user_login = browser.find_element(By.XPATH, '//*[@id="user-name"]')
        user_login.send_keys('locked_out_user')

        user_pass = browser.find_element(By.XPATH, '//*[@id="password"]')
        user_pass.send_keys('secret_sauce')

        button = browser.find_element(By.XPATH, '//*[@id="login-button"]')
        button.click()
        time.sleep(3)

    def test_problem(self, browser):
        browser.get(link)

        user_login = browser.find_element(By.XPATH, '//*[@id="user-name"]')
        user_login.send_keys('problem_user')

        user_pass = browser.find_element(By.XPATH, '//*[@id="password"]')
        user_pass.send_keys('secret_sauce')

        button = browser.find_element(By.XPATH, '//*[@id="login-button"]')
        button.click()
        time.sleep(3)

    def test_glitch(self, browser):
        browser.get(link)

        user_login = browser.find_element(By.XPATH, '//*[@id="user-name"]')
        user_login.send_keys('performance_glitch_user')

        user_pass = browser.find_element(By.XPATH, '//*[@id="password"]')
        user_pass.send_keys('secret_sauce')

        button = browser.find_element(By.XPATH, '//*[@id="login-button"]')
        button.click()
        time.sleep(3)




