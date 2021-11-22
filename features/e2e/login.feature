Feature: Log In

  Scenario: Verify Main Page of Hudl

    Given user is on the main page
    When user starts verifying the main page
    Then user successfully verified all the links and icons in the main page

  Scenario: Verify user able to login to their Hudl account

    Given user is on login page
    When user enters correct username and password
    Then user logged in successfully
    Then user logged out

  Scenario: Verify the error message when user enters wrong details

    Given user is on login page
    When user enters wrong username and password
    Then user should see error message displayed
