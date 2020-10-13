"""
Abre la pagina: https://www.google.com/
Verifica que la URL sea la correct
Encuentra el elemento con el siguiente:
NAME = q
Escribe cualquier búsqueda
Cierra el navegador
"""
from solutions.module_11.webdriver_factory import create_driver_instance

driver = create_driver_instance('chrome')
driver.implicitly_wait(15)
driver.get('https://www.google.com/')

# Test Case 1
if driver.title == 'Google':
    print('[PASS] TITLE')
else:
    print('[FAIL] TITLE')

# Test Case 2
if driver.current_url == 'https://www.google.com/':
    print('[PASS] URL')
else:
    print('[FAIL] URL')

# Search something
search_tex_box = driver.find_element_by_name('q')
search_tex_box.clear()
search_tex_box.send_keys('Selenium')

# Close Driver
driver.close()
