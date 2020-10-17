"""
Abre Firefox/Chrome
Abre https://www.amazon.com.mx/
Encuentra el dropdown con el ID “searchDropdownBox”
Crea una nueva instancia de Select para interactuar con el dropdown.
Imprime todos los elementos
Imprimir si es de selección múltiple
Imprime el elemento seleccionado actualmente
Selecciona el elemento con el índice 0
Selecciona el elemento con el texto Auto
"""
from solutions.module_11.webdriver_factory import create_driver_instance
from selenium.webdriver.support.ui import Select

# Create driver instance
driver = create_driver_instance('chrome')
driver.implicitly_wait(3)
driver.get('https://www.amazon.com.mx/')

dropdown = Select(driver.find_element_by_id('searchDropdownBox'))

print('*' * 80)
print('Dropdown options')
for index, option in enumerate(dropdown.options):
    print(f'\t{index}: {option.text}')

print('*' * 80)
print(f'Multiple: {dropdown.is_multiple}')

print('*' * 80)
print(f'First selected option: {dropdown.first_selected_option.text}')


dropdown.select_by_index(0)
dropdown.select_by_visible_text('Auto')

driver.quit()
