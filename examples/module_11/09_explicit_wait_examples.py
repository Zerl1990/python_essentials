import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
CHROME_PATH = os.path.join(ROOT_DIR, 'drivers', 'chromedriver.exe')

driver = webdriver.Chrome(executable_path=CHROME_PATH)
driver.implicitly_wait(20)
wait = WebDriverWait(driver, 5)

driver.get('https://www.phptravels.net/home')

checkin = wait.until(EC.visibility_of_element_located((By.ID, 'checkin')))
checkin.clear()
checkin.send_keys('10/11/2020')

checkout = wait.until(EC.visibility_of_element_located((By.ID, 'checkout')))
checkout.clear()
checkout.send_keys('10/11/2020')

search = wait.until(EC.element_to_be_clickable((By.XPATH, "//form[@name='HOTELS']//button[@type='submit']")))
search.submit()

driver.quit()
