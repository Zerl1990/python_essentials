"""
Abre Firefox o Chrome
Abre la pagina https://www.mercadolibre.com.mx/
Encuentra el elemento para escribir búsquedas, utiliza name
Escribe Selenium con send_keys
Encuentra el botón de buscar, utiliza class
Da click a search
Encuentra el primer resultados, utiliza class (Hint: ui-search-result__wrapper)
Da click en el producto
"""
import time

from selenium.common.exceptions import NoSuchElementException
from solutions.module_11.webdriver_factory import create_driver_instance


driver = create_driver_instance('chrome')
driver.implicitly_wait(3)
try:
    driver.get('https://www.mercadolibre.com.mx/')

    search = driver.find_element_by_name('as_word')
    search.send_keys('Selenium')

    search_btn = driver.find_element_by_class_name("nav-search-btn")
    search_btn.submit()

    time.sleep(2)
    results = driver.find_elements_by_class_name("ui-search-result__wrapper")
    print(f'Total products: {len(results)}')
    results[0].click()
except NoSuchElementException:
    print('FAILED')
finally:
    driver.quit()
