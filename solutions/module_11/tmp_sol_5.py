import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
CHROME_PATH = os.path.join(ROOT_DIR, 'drivers', 'chromedriver.exe')

driver = webdriver.Chrome(executable_path=CHROME_PATH)

driver.implicitly_wait(0)
driver.get('https://www.amazon.com.mx/')

print('A Elements:')
a_lst = driver.find_elements_by_xpath('//a')
for index, element in enumerate(a_lst):
    print(f"\t[{index}] - {element.text} - {element.get_attribute('href')}")

print('Head child elements:')
head_child = driver.find_elements_by_xpath('//head/*')
for index, element in enumerate(head_child):
    print(f"\t[{index}] - {element.text} - {element.get_attribute('href')}")

driver.quit()
