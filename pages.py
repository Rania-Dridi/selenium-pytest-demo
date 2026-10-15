"""Page objects for https://www.saucedemo.com (a public demo shop made for test practice)."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://www.saucedemo.com"


class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))


class LoginPage(BasePage):
    USER = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        self.driver.get(BASE_URL)
        return self

    def login(self, user: str, password: str):
        self.visible(self.USER).send_keys(user)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.SUBMIT).click()

    def error_text(self) -> str:
        return self.visible(self.ERROR).text


class InventoryPage(BasePage):
    ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT = (By.CLASS_NAME, "product_sort_container")
    PRICES = (By.CLASS_NAME, "inventory_item_price")

    def item_count(self) -> int:
        self.visible(self.ITEMS)
        return len(self.driver.find_elements(*self.ITEMS))

    def add_first_items(self, n: int):
        self.visible(self.ITEMS)
        for button in self.driver.find_elements(*self.ADD_BUTTONS)[:n]:
            button.click()

    def cart_count(self) -> int:
        badges = self.driver.find_elements(*self.CART_BADGE)
        return int(badges[0].text) if badges else 0

    def sort_by(self, value: str):
        from selenium.webdriver.support.ui import Select

        Select(self.visible(self.SORT)).select_by_value(value)

    def prices(self) -> list[float]:
        return [float(e.text.replace("$", "")) for e in self.driver.find_elements(*self.PRICES)]

    def open_cart(self):
        self.driver.find_element(*self.CART_LINK).click()


class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def item_count(self) -> int:
        self.visible((By.CLASS_NAME, "cart_list"))
        return len(self.driver.find_elements(*self.CART_ITEMS))
