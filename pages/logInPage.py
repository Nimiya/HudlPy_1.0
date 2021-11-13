import time

from screens.loginPageScreen import LogInPageElements
from config.browser import Browser
from pages.Actions.actions import Actions
import json


class LoginPage(Browser):

    @staticmethod
    def login():
        cred_json = open('strategy/loginCredentials.json')
        credentials = json.load(cred_json)
        username = credentials['username']
        password = credentials['password']
        Actions.send_keys(LogInPageElements.loginPage_email_txtbox, username)
        Actions.send_keys(LogInPageElements.loginPage_password_txtbox, password)
        Actions.click(LogInPageElements.loginPage_logIn_btn)

    @staticmethod
    def verifySuccessLogin():
        time.sleep(1)
        title = Browser.driver.title
        titles_json = open('strategy/titles.json')
        titles = json.load(titles_json)
        if title == titles['homeHudl']:
            status = True
        else:
            status = False
        if not status:
            assert False, "Title not found - Test failed"
        else:
            assert status is True
            assert True, "Test Passed"

    @staticmethod
    def enterWrongLoginCredentials():
        cred_json = open('strategy/loginCredentials.json')
        credentials = json.load(cred_json)
        username = credentials['wrongUserName']
        password = credentials['wrongPassword']
        Actions.send_keys(LogInPageElements.loginPage_email_txtbox, username)
        Actions.send_keys(LogInPageElements.loginPage_password_txtbox, password)
        Actions.click(LogInPageElements.loginPage_logIn_btn)

    @staticmethod
    def verifyErrorMessage():
        Actions.is_displayed(LogInPageElements.loginPage_error_lbl)