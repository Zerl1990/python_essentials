import os


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
CHROME_PATH = os.path.join(ROOT_DIR, 'drivers', 'chromedriver.exe')

driver = webdriver.Chrome(executable_path=CHROME_PATH)
driver.get('https://www.amazon.com.mx/')
# NO IMPLICIT WAIT - 0

wait = WebDriverWait(driver, 10)
dropdown = wait.until(EC.visibility_of_element_located((By.ID, 'searchDropdownBox')))
wait.until(EC.element_to_be_clickable((By.ID, 'searchDropdownBox')))
wait.until(EC.presence_of_element_located((By.ID, 'nav-search-submit-text')))
