"""
Crea una nueva instancia de FirefoxDriver
Abre la pagina de google.com
Muévete a la página de facebook
Muévete a la pagina de ESPN
Muévete hacia atrás dos veces e imprime la URL actual
Muévete hacia adelante una vez e imprime la URL actual
Refresca la página actual e imprime la URL actual
Cierra el navegador
"""
import os
from selenium import webdriver


ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
CHROME_PATH = os.path.join(ROOT_DIR, 'drivers', 'chromedriver.exe')

chrome_driver = webdriver.Chrome(executable_path=CHROME_PATH)

chrome_driver.get('https://google.com')
chrome_driver.get('https://www.facebook.com/')
chrome_driver.get('https://www.espn.com.mx/')
chrome_driver.back()
chrome_driver.back()
print(f'URL: {chrome_driver.current_url}')
chrome_driver.forward()
print(f'URL: {chrome_driver.current_url}')
chrome_driver.refresh()
print(f'URL: {chrome_driver.current_url}')
chrome_driver.quit()
