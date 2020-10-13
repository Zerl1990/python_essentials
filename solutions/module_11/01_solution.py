import os

from selenium import webdriver


ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
CHROME_PATH = os.path.join(ROOT_DIR, 'drivers', 'chromedriver.exe')


chrome_driver = webdriver.Chrome(executable_path=CHROME_PATH)

chrome_driver.get('https://google.com')
print(chrome_driver.title)
print(chrome_driver.current_url)
print(chrome_driver.page_source)
chrome_driver.quit()
