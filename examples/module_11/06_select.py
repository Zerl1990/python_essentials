import os

from selenium import webdriver
from selenium.webdriver.support.ui import Select

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
CHROME_PATH = os.path.join(ROOT_DIR, 'drivers', 'chromedriver.exe')


chrome_driver = webdriver.Chrome(executable_path=CHROME_PATH)
chrome_driver.implicitly_wait(10)
chrome_driver.get('https://www.amazon.com.mx/')
select = Select(chrome_driver.find_element_by_id('searchDropdownBox'))
select.select_by_visible_text('Auto')
chrome_driver.close()
