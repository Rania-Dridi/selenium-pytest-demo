# selenium-pytest-demo

End-to-end web tests with Selenium and pytest, using the Page Object pattern, against
[saucedemo.com](https://www.saucedemo.com), a public shop built for test practice.

Complements my [DemoQA_TestProject](https://github.com/Rania-Dridi/DemoQA_TestProject).

## What is covered

- Login: success, locked-out user, wrong password, empty fields (parametrized)
- Catalog: six products displayed
- Cart: adding items updates the badge and the cart page
- Sorting: price low to high

## Structure

| File | Role |
|------|------|
| `pages.py` | Page objects (`LoginPage`, `InventoryPage`, `CartPage`), explicit waits only |
| `conftest.py` | Chrome driver fixture (headless by default, `HEADED=1` to watch), screenshot on failure |
| `test_shop.py` | Test scenarios |

## Run

```bash
pip install -r requirements.txt
pytest -v
```

Requires Google Chrome. Selenium Manager downloads the matching driver automatically.
