import re
from playwright.sync_api import Playwright, sync_playwright, expect

firstname = "firstname-input"
lastname = "lastname-input"
email = "email-input"
birthdate = "birthdate-input"
avtar = "link", name="10"
password ="password-input"
login_button = "button", name="LogIn"


def test_register(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:3000/")
    page.get_by_test_id("btn-dropdown").click()
    page.get_by_role("link", name="Register").click()
    page.get_by_test_id("firstname-input").click()
    page.get_by_test_id("firstname-input").fill("firstname")
    page.get_by_test_id("lastname-input").click()
    page.get_by_test_id("lastname-input").fill("lastname")
    page.get_by_test_id("email-input").click()
    page.get_by_test_id("email-input").fill("lictsr@gmail.com")
    page.get_by_test_id("birthdate-input").click()
    page.get_by_role("link", name="10").click()
    page.get_by_test_id("password-input").click()
    page.get_by_test_id("password-input").fill("malli123")
    page.get_by_role("combobox").select_option("00a075fb-dc86-4b6a-bfd9-d092273a81e9.jpg")
    page.locator("#userPicture").click(button="right")
    page.locator("#userPicture").click()
    page.get_by_test_id("register-button").click()
    page.get_by_role("textbox", name="Enter User Email").click()
    page.get_by_role("textbox", name="Enter User Email").fill("lictsr@gmail.com")
    page.get_by_role("textbox", name="Enter Password").click()
    page.get_by_role("textbox", name="Enter Password").fill("malli123")
    page.get_by_role("textbox", name="Enter Password").press("Enter")
    page.get_by_role("button", name="LogIn").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
