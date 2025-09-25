from pytest-bdd import scenario,given,when,then
Feature: User Registration

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

@scenario('register_user.feature' ,'As a new user,I should be able to register to log in')
def register_user():
  pass
@given( 'I opened the GAD launch page')
def launch_gad('url'):
  pass
@given('I hovered on Login icon and clicked Register option')
def invoke_register():
  pass
@given('And User Registration form is Launched)')
def form_invoked():
  pass
@when('I entered user <firstname>')
  def enter_firstname(firstname):
    pass

