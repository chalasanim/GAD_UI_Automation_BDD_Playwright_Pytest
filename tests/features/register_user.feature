Feature: User Registration
<<<<<<< steps
  Examples: 
    | firstname | lastname | email 			| birthdate  | avtar   |
    | test      | test     | test@mail.com  | 10/10/1910 | xxxxx   |
=======

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
