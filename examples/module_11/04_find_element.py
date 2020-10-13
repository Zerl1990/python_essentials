import os

from selenium import webdriver


ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
CHROME_PATH = os.path.join(ROOT_DIR, 'drivers', 'chromedriver.exe')


chrome_driver = webdriver.Chrome(executable_path=CHROME_PATH)

chrome_driver.get('https://www.facebook.com/')

email_text_box = chrome_driver.find_element_by_id('email')
print(f'Email text: {email_text_box.text}')
print(email_text_box.clear())
print(email_text_box.send_keys('luis.rivas.0606@gmail.com'))
print(f'Email text: {email_text_box.text}')
chrome_driver.close()

