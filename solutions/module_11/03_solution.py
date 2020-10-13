import os
import time


from selenium import webdriver


ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
CHROME_PATH = os.path.join(ROOT_DIR, 'drivers', 'chromedriver.exe')

chrome_driver = webdriver.Chrome(executable_path=CHROME_PATH)
chrome_driver.implicitly_wait(10)
chrome_driver.get('https://www.youtube.com/')


search_text_box = chrome_driver.find_element_by_id('search-container')
print(f'Search text box displayed: {search_text_box.is_displayed()}')
print(f'Search text box active: {search_text_box.is_enabled()}')
# search_text_box.send_keys('Selenium')

search_btn = chrome_driver.find_element_by_id('search-icon-legacy')
search_btn.click()
time.sleep(5)

chrome_driver.quit()
