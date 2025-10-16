from .BasePage import BasePage
from playwright.sync_api import Page, Locator
import re

class RegisterUserPage(BasePage):

    def __init__(self, page : Page):
        super().__init__(page)
        # Registration Form
        self.firstname_test_id = "firstname-input"
        self.lastname_test_id = "lastname-input"  
        self.email_test_id = "email-input"
        self.password_test_id = "password-input"  
        self.birth_date="birthdate-input"
        self.doneBtn = {"role": "button", "name": "Done"}
        self.profile_combobox = {'role': 'combobox', 'name':'avatar'}
        self.user_picture = "#userPicture"
        self.registerbtn ="register-button"
        self.alert_popup = {'role': 'alert', 'name' : 'alert-popup'}

        
    @property
    def FirstName(self) -> Locator:
        return self.locator(self.firstname_test_id)
           
    @property
    def LastName(self) -> Locator:           
        return self.locator(self.lastname_test_id)
    @property
    def Email(self) -> Locator:
        return self.locator(self.email_test_id)  
    @property
    def BirthDate(self) -> Locator:
        return self.locator(self.birth_date)      
    @property
    def Password(self) -> Locator:
        return self.locator(self.password_test_id)        
    @property
    def Register(self) -> Locator:
        return self.locator(self.registerbtn)
    @property
    def Profile_Combobox(self) -> Locator:
        return self.locator(self.profile_combobox)
    @property
    def DoneButton(self) -> Locator:
        return self.locator(self.doneBtn)
    @property   
    def User_Picture(self) -> Locator:
         return self.locator(self.user_picture)
    @property 
    def AlertPopup(self) -> Locator:
        return self.locator(self.alert_popup)

    


   
    def enter_firstname(self, firstname: str):
        self.FirstName.fill(firstname)       

    def enter_lastname(self, lastname: str):
        self.LastName.fill(lastname)  

    def enter_email(self, email: str):
        self.Email.fill( email)

    def enter_birthdate(self, birthdate: str):
        self.BirthDate.fill(birthdate)  

    def click_done_btn(self):
        self.DoneButton.click()

    def enter_password(self, password: str):
        self.Password.fill(password)  

    def select_profile_image(self, image_value: str):
        self.Profile_Combobox.select_option(image_value)

    def click_register(self):
        self.Register.click()



    def get_alert_message(self) :
        self.page.screenshot(path="screenshot.png")

    

  
            



                    
    





  