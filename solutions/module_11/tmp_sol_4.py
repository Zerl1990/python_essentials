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

driver.get('https://www.phptravels.net/home')

wait = WebDriverWait(driver, 20)
locator = (By.ID, 'INVALID')
start = time.time()
try:
    element = wait.until(EC.element_to_be_clickable(locator))
except Exception:
    pass
print(f'Total Wait Time: {time.time() - start} seconds')
driver.quit()
