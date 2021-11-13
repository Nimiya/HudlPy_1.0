from selenium import webdriver


class Browser(object):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, executable_path=r'drivers/chromedriver.exe')
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(self):
        self.driver.close()
