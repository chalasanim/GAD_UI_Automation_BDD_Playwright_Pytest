from playwright.sync_api import  Locator,Page, expect, TimeoutError as PlaywrightTimeoutError


class BasePage:

    def __init__(self, page :Page):

        self.page = page                  

    def locator(self, selector: str) -> Locator:       
  
        if  'role' in selector and 'name' in selector:
            return self.page.get_by_role(selector['role'], name=selector['name'])    
        elif 'id'   in selector :
             return  self.page.locator(f"#{selector['id']}")  
        else:
            return self.page.get_by_test_id(selector)
    
    def click(self, selector: locator):
        if isinstance(selector, Locator):
             self.page.locator(selector).click()
        else:
            raise ValueError("Selector must be a Locator instance")        
        

    def navigate(self, url):

        self.page.goto(url)
        

    def getTitle(self):

        return self.page.title()

    def getPageUrl(self):

        return self.page.url
    

    def waitForPage(self):
        pass
