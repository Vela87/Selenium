from selenium.webdriver.common.by import By


class ThirdPage:

    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "[id='checkout']").click()
        assert self.driver.find_element(By.ID, 'continue').is_displayed()
