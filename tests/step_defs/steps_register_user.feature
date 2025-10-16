from pytest-bdd import scenario,given,when,then
Feature: User Registration

  Examples: 
    | firstname | lastname | email 			| birthdate  | avtar   |
    | test      | test     | test@mail.com  | 10/10/1910 | xxxxx   |



@scenario('register_user.feature','As a new user,I should be able to register to log in')
def register_user():
  pass
@given('I opened the GAD launch page')
def launch_gad('url'):
  pass
@given('I hovered on Login icon and clicked Register option')
def invoke_register():
  pass
@given('And User Registration form is Launched)'
def form_invoked():
  pass
@when('I entered user <firstname>')
  def enter_text_field(firstname):
    pass
@when('I entered user <lastname>')
   def enter_text_field(lastname):
      pass
@when('I entered user <email>')
   def enter_text_field(email):
      pass
@when('I entered user <birthdate>')
   def enter_date_field(birthdate):
      pass
@when('I entered user <password>')
   def enter_password(password):
      pass
@when('I selected user <avtar>')
   def select_user_avatar(avtar):
      pass
@when(' And I clicked <register> button')
   def click_buton(button):
      pass
   
@then ('User created <message> displayed')
   def check_label(text):
      pass
@then ('the <login> screen is launnched')
   def check_form(form):
      pass

  
  