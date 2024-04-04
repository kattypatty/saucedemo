import time

# Locators
TITLE = ("css selector", "div[class='product_label']")
INVENTORY_ITEMS = ("css selector", "div[class='inventory_item']")

# Test Login
def test_login_positive(driver): 

# Checking the actual title of the main page
    actual_title = driver.find_element(*TITLE).text
    expected_title = "Products"
    assert actual_title == expected_title, f"Unexpected text, expected text: {expected_title},actual text: {actual_title} "

# Checking the number of items on the main page
    items_list = driver.find_elements(*INVENTORY_ITEMS)
    expected_items = 6
    assert len(items_list) == expected_items, f"Expected: {expected_items}, actual: {len(items_list)}"
    time.sleep(3)

def test_login_negative(driver):
    driver.get("https://www.saucedemo.com/v1/index.html")
# Wrong username
    assert driver.title == "Swag Labs"
    assert driver.find_element("css selector", 'h3').text == "Epic sadface: Sorry, this user"
