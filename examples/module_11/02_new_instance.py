import os

from selenium import webdriver


ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
CHROME_PATH = os.path.join(ROOT_DIR, 'drivers', 'chromedriver.exe')
FIREFOX_PATH = os.path.join(ROOT_DIR, 'drivers', 'geckodriver.exe')


# Chrome browser
chrome_driver = webdriver.Chrome(executable_path=CHROME_PATH)
chrome_driver.close()

# Chrome browser
firefox_driver = webdriver.Firefox(executable_path=FIREFOX_PATH)
firefox_driver.close()
