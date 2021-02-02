import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select


ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
CHROME_PATH = os.path.join(ROOT_DIR, 'drivers', 'chromedriver.exe')

driver = webdriver.Chrome(executable_path=CHROME_PATH)
driver.implicitly_wait(10)

driver.get('https://formsmarts.com/form/axi?mode=h5')


first_name = driver.find_element_by_id('u_wJI_60857')
last_name = driver.find_element_by_id('u_wJI_60858')
email = driver.find_element_by_id('u_wJI_60859')
address = driver.find_element_by_id('u_wJI_60860')
country_dropdown = Select(driver.find_element_by_id('u_wJI_60871'))
checkin = driver.find_element_by_id('u_wJI_60861')
nights = driver.find_element_by_id('u_wJI_60870')
continue_btn = driver.find_element_by_class_name('button-primary')

first_name.send_keys('Luis')
last_name.send_keys('Rivas')
email.send_keys('luis.rivas.0606@gmail.com')
address.send_keys('DEMO')
country_dropdown.select_by_value('MX')
country_dropdown.select_by_visible_text('Mexico')
checkin.send_keys('11/18/2020')
nights.send_keys('5')
continue_btn.click()

driver.quit()
