@smoke @atm
Feature: User Registration
  
Scenario Outline: As a new user,I should be able to register to log in.
  Given I opened the GAD launch page
    And I hovered on Login icon and clicked Register option
    And User Registration form is Launched
   When I entered user <firstname>
   	And I entered user <lastname>
    And I entered user <email>
    And I entered user <birthdate>
    And I entered user <password>
    And I selected user <avtar>
    And I clicke <register> button    	  
   Then User created messaged displayed 
    And the login screen is launnched
  Examples: 
    | firstname | lastname | email 			| birthdate  | avtar   |
    | test      | test     | test@mail.com  | 10/10/1910 | xxxxx   |
  
  