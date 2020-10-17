"""
Abre Firefox/Chrome.
Abre https://es.wikipedia.org/wiki/Wikipedia:Portada
Encuentra el elemento que contiene en su link: “Portada”.
Imprime el contenido de href
Encuentra todos los elementos con el tag “button”
Imprime el texto en cada uno de los elementos
Encuentra todos los elementos con el tag “p”
Imprime el total de elementos
Obtener el texto de cada elemento
Create un histograma de palabras únicas
Imprime los elementos del índice 2 y 12, dando incrementos de 4 en 4
"""
from solutions.module_11.webdriver_factory import create_driver_instance


# Create driver instance
driver = create_driver_instance('chrome')
driver.implicitly_wait(3)
driver.get('https://es.wikipedia.org/wiki/Wikipedia:Portada')

# Find portada
link = driver.find_element_by_link_text('Portada')
print(f"Link href: {link.get_attribute('href')}")

# Button text
print(f'Button text:')
btn_list = driver.find_elements_by_tag_name('button')
for btn in btn_list:
    print(f'\t{btn.text}')

# Histogram
p_list = driver.find_elements_by_tag_name('p')
print('*' * 80)
print('P histogram')
hist = {}
for item in p_list:
    for word in item.text.split(' '):
        if word not in hist:
            hist[word] = 1
        else:
            hist[word] += 1
print(hist)

# P slicing
print('*' * 80)
print('P between 2-13, step 4')
for item in p_list[2:13:4]:
    print(f'\t{item.text}')

driver.quit()
