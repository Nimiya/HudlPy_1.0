from screens.homePageScreen import HomePageElements
from config.browser import Browser

from pages.Actions.actions import Actions
import json


class HomePage(Browser):

    @staticmethod
    def navigateToHudlHomePage():
        url_json = open('config/url.json')
        url = json.load(url_json)
        Actions.get(url['hudl'])

    @staticmethod
    def verifyHudlLogo():
        Actions.is_displayed(HomePageElements.homepage_hudlLogo_img)

    @staticmethod
    def verifyTitleOfHomePage():
        title = Actions.title()
        titles_json = open('strategy/titles.json')
        titles = json.load(titles_json)
        if title == titles['hudlTitle']:
            status = True
        else:
            status = False
        if not status:
            assert False, "Title not found - Test failed"
        else:
            assert status is True
            assert True, "Test passed"

    @staticmethod
    def verifyHighSchoolLinkDisplayedInHomePage():
        Actions.is_displayed(HomePageElements.homepage_highSchool_lnk)

    @staticmethod
    def verifyDivisionLinkDisplayedInHomePage():
        Actions.is_displayed(HomePageElements.homePage_division_lnk)

    @staticmethod
    def verifySupportLinkDisplayedInHomePage():
        Actions.is_displayed(HomePageElements.homePage_support_lnk)

    @staticmethod
    def clickOnLogInButton():
        Actions.click(HomePageElements.homePage_logIn_btn)
