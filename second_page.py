from selenium.webdriver.common.by import By


class SecondPage:

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "[id='add-to-cart-sauce-labs-backpack']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[class='shopping_cart_badge']").click()
        assert self.driver.find_element(By.CLASS_NAME, 'cart_desc_label').is_displayed()
