from .BasePage import BasePage
from playwright.sync_api import Page, Locator

class LoginPage(BasePage):

    def __init__(self, page : Page):
      super().__init__(page)
      self.LOGINBUTTON = {"role": "button", "name": "LogIn"}
        # Login Form
      self.LOGIN_EMAIL_INPUT = {"role": "textbox", "name": "Enter User Email"}
      self.LOGIN_PASSWORD_INPUT = {"role": "textbox", "name": "Enter Password"}
      if self.page.title() != "🦎 GAD | Login":
            self.page.goto("http://localhost:3000/login")
            #raise Exception("This is not the Login page. Current page is: " + self.page.title())    

    @property
    def login_button(self) -> Locator:
     return self.locator(self.LOGINBUTTON)
        
    @property
    def login_email_input(self) -> Locator:
        return self.locator(self.LOGIN_EMAIL_INPUT)
        

    @property
    def login_password_input(self) -> Locator:
        return self.locator(self.LOGIN_PASSWORD_INPUT)
        

    def enter_username(self,struser) :
        self.login_email_input.fill(struser)

    def enter_password(self,strpwd) :
        self.login_password_input.fill(strpwd)

    def click_login(self):
        self.login_button.click()