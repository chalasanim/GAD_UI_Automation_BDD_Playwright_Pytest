from .BasePage import BasePage
from playwright.sync_api import Page, Locator

class LoginPage(BasePage):

    def __init__(self, page : Page):
      super().__init__(page)
      self.login_button = self.locator({"role": "button", "name": "LogIn"})
        # Login Form
      self.login_email_input = self.locator({"role": "textbox", "name": "Enter User Email"})
      self.login_password_input = self.locator({"role": "textbox", "name": "Enter Password"})
      if self.page.title() != "🦎 GAD | Login":
            self.page.goto("http://localhost:3000/login")
            #raise Exception("This is not the Login page. Current page is: " + self.page.title())    



        
           

    def enter_username(self,struser) :
        self.login_email_input.fill(struser)

    def enter_password(self,strpwd) :
        self.login_password_input.fill(strpwd)

    def click_login(self):
        self.login_button.click()
        self.page.screenshot(path="screenshot.png")

        



    