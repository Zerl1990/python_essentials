import os


from selenium import webdriver


__ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
__CHROME_PATH = os.path.join(__ROOT_DIR, 'drivers', 'chromedriver.exe')
__FIREFOX_PATH = os.path.join(__ROOT_DIR, 'drivers', 'geckodriver.exe')


def create_driver_instance(browser_name):
    if browser_name.lower() == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(executable_path=__CHROME_PATH, chrome_options=options)
    elif browser_name.lower() == 'firefox':
        firefox_driver = webdriver.Firefox(executable_path=__FIREFOX_PATH)
        firefox_driver.maximize_window()
        return driver
    else:
        raise ValueError('Invalid browser selected!')


if __name__ == '__main__':
    driver = create_driver_instance('chrome')
    driver.close()
