import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class GoogleSearch:
    def __init__(self, driver: webdriver.Chrome, timeout: int = 10):
        self.driver = driver
        self.__url = 'https://www.google.com/'
        self.__wait = WebDriverWait(driver, timeout)
        self.__submit_locator = (By.XPATH, "//*[@class='FPdoLc tfB0Bf']//*[@name='btnK']")

    def open(self):
        self.driver.get(self.__url)
        self.wait_until_loaded()

    def search(self, value):
        search_box = self.__get_search_box()
        submit_btn = self.__get_submit_btn()
        search_box.clear()
        search_box.send_keys(value)
        search_box.send_keys(Keys.TAB)
        submit_btn.click()

    def wait_until_loaded(self):
        self.__wait.until(EC.presence_of_element_located((By.NAME, 'q')))
        self.__wait.until(EC.presence_of_element_located((By.ID, 'hplogo')))

    def __get_search_box(self) -> WebElement:
        return self.__wait.until(EC.presence_of_element_located((By.NAME, 'q')))

    def __get_submit_btn(self) -> WebElement:
        return self.__wait.until(EC.presence_of_element_located(self.__submit_locator))


if __name__ == '__main__':
    ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
    CHROME_PATH = os.path.join(ROOT_DIR, 'drivers', 'chromedriver.exe')
    chrome_driver = webdriver.Chrome(executable_path=CHROME_PATH)

    # Script logic
    google = GoogleSearch(chrome_driver, 15)
    google.open()
    google.wait_until_loaded()
    google.search('Selenium')

    # close driver
    chrome_driver.close()

