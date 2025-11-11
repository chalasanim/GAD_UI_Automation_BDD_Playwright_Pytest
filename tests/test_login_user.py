import re
import random
from pages.LoginPage import LoginPage
from playwright.sync_api import expect


def test_login_user(page, user_data) -> None:
    

    login_page =LoginPage(page)


    login_page.enter_username("utes4663@gmail.com")
    login_page.enter_password("test123")
    login_page.click_login()

    expect(page.locator("#username")).to_contain_text("Hello User!")


  


