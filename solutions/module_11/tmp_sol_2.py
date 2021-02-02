import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select


ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
CHROME_PATH = os.path.join(ROOT_DIR, 'drivers', 'chromedriver.exe')

driver = webdriver.Chrome(executable_path=CHROME_PATH)
driver.implicitly_wait(10)

driver.get('https://formsmarts.com/html-form-example')
iframe = driver.find_element_by_class_name('fs_embed')
driver.switch_to.frame(iframe)

first_name = driver.find_element_by_id('u_Emn_4607')
last_name = driver.find_element_by_id('u_Emn_338354')
email = driver.find_element_by_id('u_Emn_4608')
inquiry = driver.find_element_by_id('u_Emn_4609')
continue_btn = driver.find_element_by_class_name('button-primary')
subject_dropdown = Select(driver.find_element_by_id('u_Emn_338367'))


first_name.send_keys('Luis')
last_name.send_keys('Rivas')
email.send_keys('luis.rivas.0606@gmail.com')
inquiry.send_keys('DEMO')
subject_dropdown.select_by_value('Sales Inquiry')
continue_btn.click()

driver.quit()
