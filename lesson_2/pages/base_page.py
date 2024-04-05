class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # opening webrowser
    def open(self):
        self.driver.get(self.url)

    # getting text to check the actual title of the home page
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    # getting the length or number of inventory cards on the home page
    def get_lenght(self, locator):
        return len(self.driver.find_elements(*locator))