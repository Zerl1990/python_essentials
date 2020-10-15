"""
Abre Firefox/Chrome.
Abre https://www.nasa.gov/.
Encuentra el elemento con el link: “/topics/humans-in-space'.
Imprime el contenido de href (Hint: Puedes utilizar get_attribute(attribute_name)).
Encuentra el elemento que contiene en su link: “nasatv”.
Imprime el contenido de href
Encuentra todos los elementos con el tag a  ***slicing review/dictionaries***
Imprime el total de elementos
Crea un histograma de los links
Imprime los links del índice 0 al 20, dando incrementos de 3 en 3
"""
from solutions.module_11.webdriver_factory import create_driver_instance


# Create driver instance
driver = create_driver_instance('chrome')
driver.implicitly_wait(3)
driver.get('https://www.nasa.gov/')

# Get human in space link
humans_in_space = driver.find_element_by_link_text('Humans in Space')
print(f"Human in space: {humans_in_space.get_attribute('href')}")

# Get NASA TV link
nasa_tv = driver.find_element_by_partial_link_text('NASA TV')
print(f"Nasa TV: {nasa_tv.get_attribute('href')}")

# Get a tag
links = driver.find_elements_by_tag_name('a')
print(f'Total links: {len(links)}')

# Histogram
print('*' * 80)
print('Links histogram')
hist = {}
for item in links:
    href = item.get_attribute('href')
    if href not in hist:
        hist[href] = 1
    else:
        hist[href] += 1
print(hist)

# Links slicing
print('*' * 80)
print('Links between 0-20, step 3')
for item in links[0:21:3]:
    print(f"\t{item.get_attribute('href')}")

driver.quit()
