import os

from selenium import webdriver


ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
CHROME_PATH = os.path.join(ROOT_DIR, 'drivers', 'chromedriver.exe')


chrome_driver = webdriver.Chrome(executable_path=CHROME_PATH)

chrome_driver.get('https://www.facebook.com/')


element = chrome_driver.find_element_by_id('email')
chrome_driver.close()
