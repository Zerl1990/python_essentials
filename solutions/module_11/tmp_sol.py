import os

from selenium import webdriver

# C:\Users\lmrivas\Documents\QAMinds\2020_python\solutions\module_11
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
# C:\Users\lmrivas\Documents\QAMinds\2020_python\solutions\module_11\drivers\chromedriver.exe
CHROME_PATH = os.path.join(ROOT_DIR, 'drivers', 'chromedriver.exe')


chrome_driver = webdriver.Chrome(executable_path=CHROME_PATH)
chrome_driver.implicitly_wait(10)

chrome_driver.get('file:///C:/Users/lmrivas/Documents/QAMinds/2020_python/html.html')
print(chrome_driver.title)
print(chrome_driver.current_url)
print(chrome_driver.page_source)
btn = chrome_driver.find_element_by_id('MyTestBtn')

chrome_driver.find_element_by_link_text()
print(btn.is_displayed())
print(btn.is_selected())
print(btn.is_enabled())
btn.click()
chrome_driver.quit()
