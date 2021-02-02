import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
CHROME_PATH = os.path.join(ROOT_DIR, 'drivers', 'chromedriver.exe')

driver = webdriver.Chrome(executable_path=CHROME_PATH)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get('https://www.espn.com.mx/')

locator = (By.XPATH, "//a[contains(@name, 'recomendamos')]")
elements = wait.until(EC.visibility_of_all_elements_located(locator))

print(f'Total recomendados {len(elements)}')
elements[0].click()


wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Mexican Liga BBVA MX']")))
driver.back()


elements = wait.until(EC.visibility_of_all_elements_located(locator))
elements[1].click()
