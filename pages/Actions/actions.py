from config.browser import Browser


class Actions(Browser):

    def get(self):
        return Browser.driver.get(self)

    def is_displayed(self):
        try:
            Browser.driver.find_element_by_xpath(self).is_displayed()
        except:
            assert False, "Element " + self + " not found"

    def click(self):
        try:
            Browser.driver.find_element_by_xpath(self).click()
        except:
            assert False, "Element " + self + " not found or not clickable"

    @staticmethod
    def title():
        return Browser.driver.title

    def send_keys(self, value):
        try:
            Browser.driver.find_element_by_xpath(self).is_displayed()
            Browser.driver.find_element_by_xpath(self).send_keys(value)
        except:
            assert False, "Element " + self + " not found"