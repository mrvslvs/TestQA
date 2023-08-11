import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://ciricc.github.io/"


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_streaming_API(self, browser):
        print("start test1")
        browser.get(link)
        element = browser.find_element(By.XPATH, '//*[@id="main-content"]/div/ul[1]/li[5]/a[2]')
        element.click()
        print("finish test1")

    def test_locked_out_user_login(self, browser):
        print("start test2")
        browser.get(link)
        element = browser.find_element(By.XPATH, '//*[@id="main-content"]/div/p[15]/a')
        browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()
        print("finish test2")

