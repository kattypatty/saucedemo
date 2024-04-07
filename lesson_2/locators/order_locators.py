from selenium.webdriver.common.by import By

class OrderLocators:
    FIRST_NAME = ("css selector", "input[id='first-name']")
    LAST_NAME = ("css selector", "input[id='last-name']")
    ZIP_CODE = ("css selector", "input[id='postal-code']")
    CONTINUE_BTN = (By.XPATH, "//*[@class='btn_primary cart_button']")
    FINISH_BTN = (By.XPATH, "//*[@class='btn_action cart_button']")

    SUCCESSFUL_ORDER = ("css selector", "h2[class='complete-header']")
    ERROR_MESSAGE = ("css selector", "h3[data-test='error']")
    