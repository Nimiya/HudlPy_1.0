import os
import shutil

import allure
from allure_commons.types import AttachmentType
from config.browser import Browser
from pages.homePage import HomePage
from pages.logInPage import LoginPage
from pages.accountHomePage import AccountHomePage


def before_all(context):
    context.browser = Browser()
    context.homePage = HomePage()
    context.loginPage = LoginPage()
    context.accountHomePage = AccountHomePage()
    shutil.rmtree('reports')
    if not os.path.exists('reports/json'):
        os.makedirs('reports/json')
    if not os.path.exists('reports/allure-report'):
        os.makedirs('reports/allure-report')


def after_scenario(context, scenario):
    # Take screenshot if scenario fails
    if scenario.status == 'failed':
        allure.attach(context.browser.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=AttachmentType.PNG)


def after_all(context):
    if context.failed:
        context.browser.close()
    context.browser.close()
