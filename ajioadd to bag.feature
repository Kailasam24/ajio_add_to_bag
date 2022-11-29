Feature: Ajio add to bag
  Background: log in ajio application
  Given I launch browser
    When I open ajio
    When click on sign in
    And Enter valid number and OTP
    And click on login

  Scenario Outline: Add to Bag
    When click on search page and enter "<element>"
    And search element click and navigated
    When click on product and navigated
    When click on "<size>"
    And click on add to bag
    And click on go to bag and navigated
    And click on proceed to shopping

    Examples:
    | element | size |
#    | kurti   |  L   |
#    | heels   |  '6'  |
    | jacket  |  M   |
    | sargfdse@23 | FS  |
#    | b2r477j89 | L   |

