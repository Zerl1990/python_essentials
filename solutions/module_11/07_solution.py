"""
Abre la pagina de Amazon: https://www.amazon.com.mx/
Espera 10 segundos
Encuentra el campo de texto: ID = twotabsearchtextbox
Escribe “Selenium”
Envía enter
from selenium.webdriver.common.keys import Keys
send_keys(Keys.ENTER)
Espera 10 segundos
Cierra el navegador
"""
import time


from solutions.module_11.webdriver_factory import create_driver_instance
from selenium.webdriver.common.keys import Keys


driver = create_driver_instance('chrome')
driver.implicitly_wait(15)
driver.get('https://www.amazon.com.mx/')

search = driver.find_element_by_id('twotabsearchtextbox')
search.send_keys('Selenium')
search.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()
