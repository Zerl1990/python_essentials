import os

from selenium import webdriver
from selenium.webdriver.support.ui import Select

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
CHROME_PATH = os.path.join(ROOT_DIR, 'drivers', 'chromedriver.exe')


chrome_driver = webdriver.Chrome(executable_path=CHROME_PATH)
chrome_driver.implicitly_wait(10)
chrome_driver.get('https://www.amazon.com.mx/')

select_element = chrome_driver.find_element_by_id('searchDropdownBox')
select = Select(select_element)
select.select_by_visible_text('Prime Video')
select.select_by_index(5)
select.select_by_value('search-alias=fashion')
print(f"{select.first_selected_option.get_attribute('value')}")
chrome_driver.close()
