import time

from screens.accountHomePageScreen import AccountHomePageElements
from screens.homePageScreen import HomePageElements
from config.browser import Browser
from pages.Actions.actions import Actions
import json


class AccountHomePage(Browser):

    @staticmethod
    def clickLogout():
        Actions.click(AccountHomePageElements.accountHomePage_globalMenu_lnk)
        Actions.click(AccountHomePageElements.accountHomePage_logOut_lnk)

    @staticmethod
    def verifyLogout():
        Actions.is_displayed(HomePageElements.homePage_logIn_btn)
