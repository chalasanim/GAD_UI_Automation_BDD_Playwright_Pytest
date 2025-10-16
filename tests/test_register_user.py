import re
import random
from pages.MainPage import MainPage 
from pages.RegisterUserPage import RegisterUserPage
from pages.LoginPage import LoginPage

from playwright.sync_api import Playwright, sync_playwright, expect

def test_register_user(page, user_data) -> None:
    

    main_page = MainPage(page)

    main_page.click_user_avtar()
    main_page.click_register_link()
         
    register_page = RegisterUserPage(page)

    register_page.enter_firstname( user_data["firstname"])
    register_page.enter_lastname(user_data["lastname"])
    register_page.enter_email( user_data["email"])
    register_page.enter_birthdate( user_data["birthdate"])
    register_page.click_done_btn()
    register_page.enter_password(user_data["password"])
    
    #register_page.select_profile_image(user_data["profileimage"])
    register_page.click_register()  

    expect(page.get_by_test_id("alert-popup")).to_contain_text("User created")

    login_page =LoginPage(page)


    login_page.enter_username(user_data["email"])
    login_page.enter_password(user_data["password"])
    login_page.click_login()

    expect(page.locator("#username")).to_contain_text("Hello Test!")


  


