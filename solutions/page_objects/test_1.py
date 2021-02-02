from solutions.page_objects.page_object import GoogleSignIn
from solutions.page_objects.webdriver_factory import create_driver_instance


driver = create_driver_instance('chrome')
google = GoogleSignIn(driver, 'https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin')
google.get()
google.set_email('qa-minds@gmail.com')
google.close()
