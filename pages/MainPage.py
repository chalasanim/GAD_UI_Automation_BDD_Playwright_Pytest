from .BasePage import BasePage
from .RegisterUserPage import RegisterUserPage
from playwright.sync_api import  Page, Locator

class MainPage(BasePage):
    def __init__(self, page : Page):
        super().__init__(page)
        
        # Define only selector strings
        self.user_avtar_test_id = "btn-dropdown"
        self.register_link =  {'role': 'link', 'name': 'Register'}

    # Page elements as properties
    @property
    def User_Avtar(self) -> Locator:
        return self.locator(self.user_avtar_test_id)
       # return self.page.get_by_test_id(self.user_avtar_test_id )
    
    @property
    def Register_Link(self) -> Locator:
        return self.locator(self.register_link)
        #return self.page.get_by_role('link', name=self.register_link)
       
    
    def click_user_avtar(self):
        """Click dropdown button using BasePage click method"""
        self.User_Avtar.click()
    
    def click_register_link(self):
        """Click register link using BasePage click method"""
        self.Register_Link.click()  # Uses inherited click() from BasePage
    

        