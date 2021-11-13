from behave import *


@given('user is on the main page')
def launchHomePage(context):
    context.homePage.navigateToHudlHomePage()


@when('user starts verifying the main page')
def verifyHomePage(context):
    context.homePage.verifyHudlLogo()
    context.homePage.verifyTitleOfHomePage()
    context.homePage.verifyHighSchoolLinkDisplayedInHomePage()
    context.homePage.verifyDivisionLinkDisplayedInHomePage()
    context.homePage.verifySupportLinkDisplayedInHomePage()


@then('user successfully verified all the links and icons in the main page')
def successfullyVerified(context):
    assert True, "Test Passed"


@given('user is on login page')
def navigateToLoginPage(context):
    context.homePage.navigateToHudlHomePage()
    context.homePage.clickOnLogInButton()


@when('user enters correct username and password')
def login(context):
    context.loginPage.login()


@then('user logged in successfully')
def verifyLogIn(context):
    context.loginPage.verifySuccessLogin()


@then('user logged out')
def verifyLogOut(context):
    context.accountHomePage.clickLogout()
    context.accountHomePage.verifyLogout()


@when('user enters wrong username and password')
def wrongLogin(context):
    context.loginPage.enterWrongLoginCredentials()


@then('user should see error message displayed')
def verifyLogIn(context):
    context.loginPage.verifyErrorMessage()
