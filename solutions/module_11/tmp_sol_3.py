import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
CHROME_PATH = os.path.join(ROOT_DIR, 'drivers', 'chromedriver.exe')

driver = webdriver.Chrome(executable_path=CHROME_PATH)
wait = WebDriverWait(driver, 10)


driver.get('https://www.phptravels.net/home')
checkin = wait.until(EC.visibility_of_element_located((By.ID, 'checkin')))
checkin.clear()
checkin.send_keys('10/11/2020')
driver.quit()
