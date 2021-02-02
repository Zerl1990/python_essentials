from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class GoogleSignIn:
    """Control Google Sign Page."""

    __EMAIL_LOCATOR = (By.ID, 'identifierId')

    def __init__(self, driver, url, timeout=15):
        self.__driver = driver
        self.__url = url
        self.__timeout = timeout
        self.__wait = WebDriverWait(driver, self.__timeout)

    def get(self):
        """Open url in browser."""
        self.__driver.get(self.__url)

    def close(self):
        """Close browser."""
        self.__driver.close()

    def set_email(self, value: str):
        """Set email address

        :param value: Email address
        :return: None
        """
        email = self.__wait.until(EC.element_to_be_clickable(GoogleSignIn.__EMAIL_LOCATOR))
        email.send_keys(value)

    def next(self):
        raise NotImplemented()

    def restore_password(self):
        raise NotImplemented()

    def create_account(self):
        raise NotImplemented()
