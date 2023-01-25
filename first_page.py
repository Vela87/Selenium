from selenium.webdriver.common.by import By


class FirstPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.find_element(By.CSS_SELECTOR, "[id='user-name']").send_keys('standard_user')
        self.driver.find_element(By.CSS_SELECTOR, "[id='password']").send_keys('secret_sauce')
        self.driver.find_element(By.CSS_SELECTOR, "[id='login-button']").click()
        assert self.driver.find_element(By.CLASS_NAME, 'peek').is_displayed()
