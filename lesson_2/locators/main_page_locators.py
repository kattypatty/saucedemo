

class MainPage_Locators:
# Locators
    TITLE = ("css selector", "div[class='product_label']")
    INVENTORY_ITEMS = ("css selector", "div[class='inventory_item']")
    SAUCE_LABS_BACKPACK = ("css selector", "button[class='btn_primary btn_inventory']")

    CART_BTN = ("css selector", "div[id='shopping_cart_container']")

    CARD1 = ("css selector", "div[class='inventory_item']:nth-child(1)")
    CARD2 = ("css selector", "div[class='inventory_item']:nth-child(2)")
    CARD3 = ("css selector", "div[class='inventory_item']:nth-child(3)")
    CARD4 = ("css selector", "div[class='inventory_item']:nth-child(4)")
    CARD5 = ("css selector", "div[class='inventory_item']:nth-child(5)")
    CARD6 = ("css selector", "div[class='inventory_item']:nth-child(6)")

    def get_card(self, value):
        return "css selector", f"div[class='inventory_item']:nth-child({value})"
    


    