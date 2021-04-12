Feature: Exercise1 Values

  Scenario: Right count of values appears on screen with currency
    Given launch chrome browser
    When open the exercise1 values page
    Then Verify the right count of values appears on screen with currency
    And close the browser


  Scenario: The value on the screen is greater than '0'
    Given launch chrome browser
    When open the exercise1 values page
    Then Verify the value on the screen is greater than '0'
    And close the browser

  Scenario: The correct total balance
    Given launch chrome browser
    When open the exercise1 values page
    Then Verify the total balance is correct based on the value listed on screen
    And close the browser

  Scenario: The total val matches the sum of values
    Given launch chrome browser
    When open the exercise1 values page
    Then Verify the total val matches the sum of values
    And close the browser


