"""
Abre la pagina de facebook: https://www.facebook.com/
Encuentra el campo de texto:  ID = email
Escribe tu correo
Encuentra el campo de texto: ID = pass
Escribe tu contraseña
Encuentra el botón: NAME = login
Da click al boton de Login
Espera 5 segundos
Cierra el Navegador
"""
import time


from solutions.module_11.webdriver_factory import create_driver_instance


driver = create_driver_instance('chrome')
driver.implicitly_wait(15)
driver.get('https://www.facebook.com/')

email = driver.find_element_by_id('email')
password = driver.find_element_by_id('pass')
submit_btn = driver.find_element_by_name('login')

email.send_keys('qa_minds@oracle.com')
password.send_keys('testing')
submit_btn.click()
time.sleep(5)

driver.quit()
