import pytest

from pages import CartPage, InventoryPage, LoginPage

VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"  # published on the demo site's login page


@pytest.fixture
def inventory(driver):
    LoginPage(driver).open().login(VALID_USER, VALID_PASSWORD)
    return InventoryPage(driver)


def test_login_success_shows_catalog(inventory):
    assert inventory.item_count() == 6


@pytest.mark.parametrize(
    "user, password, message",
    [
        ("locked_out_user", VALID_PASSWORD, "locked out"),
        (VALID_USER, "wrong", "do not match"),
        ("", "", "Username is required"),
    ],
)
def test_login_errors(driver, user, password, message):
    page = LoginPage(driver).open()
    page.login(user, password)
    assert message in page.error_text()


def test_add_to_cart_updates_badge_and_cart(inventory, driver):
    inventory.add_first_items(2)
    assert inventory.cart_count() == 2
    inventory.open_cart()
    assert CartPage(driver).item_count() == 2


def test_sort_price_low_to_high(inventory):
    inventory.sort_by("lohi")
    prices = inventory.prices()
    assert prices == sorted(prices)
