import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
CHROME_PATH = os.path.join(ROOT_DIR, 'drivers', 'chromedriver.exe')

driver = webdriver.Chrome(executable_path=CHROME_PATH)
wait = WebDriverWait(driver, 10)
driver.get('https://www.netflix.com/')

# Landing Page
sign_in_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Sign In')))
sign_in_link.click()


# Login From
email = wait.until(EC.element_to_be_clickable((By.ID, 'id_userLoginId')))
password = wait.until(EC.element_to_be_clickable((By.ID, 'id_password')))
sign_in = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'login-button')]")))
email.send_keys('test@gmail.com')
password.send_keys('test')
driver.quit()
