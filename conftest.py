import pytest
import random
import configparser
import logging
from playwright.sync_api import sync_playwright


logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

config = configparser.ConfigParser()
try:
    config.read("config.ini")
    browser_name = config["playwright"]["browser"].strip()
    headless_mode = config.getboolean("playwright","headless")
    slow_mo = config.getint("playwright","slow_mo", fallback=0)
    base_url = config["playwright"]["base_url"].strip()

    logger.info( " ")
except Exception as e:
    logger.error(f"Error reading config.ini:{str(e)}")
    pytest.fail(f"Configuration error: {str(e)}")


@pytest.fixture(scope="session")
def user_data():
    """Fixture that provides user data with dynamic email"""
    first_name = "Test"
    last_name = "User"
    password = "afasfsad"
    birthdate= "1981-10-10"
    profile_image = "00a075fb-dc86-4b6a-bfd9-d092273a81e9.jpg"    
    
    # Generate unique email
    number = random.randrange(1000, 9999)
    email = f"{first_name[0].lower()}{last_name[:3].lower()}{number+1000}@gmail.com"
    return {"firstname":first_name,
            "lastname":last_name,
            "password":password,
            "birthdate":birthdate,
            "profileimage":profile_image,
            "email":email}

@pytest.fixture(scope="session")
def playwright():
    """Fixture to manage Playwright instance."""
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    browser = getattr(playwright, browser_name).launch(headless=headless_mode)
    yield browser
    browser.close()


@pytest.fixture(scope="session")
def browser_context(browser, playwright):
    """Fixture to manage browser context."""
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture
def page(browser_context, playwright):
    """Fixture to manage page instance."""
    browser = getattr(playwright, browser_name).launch(headless=headless_mode)

    context = browser.new_context()
    page = context.new_page()
    page.goto(base_url)
    yield page
    context.close()
    browser.close()

@pytest.fixture(scope="session")
def app_config():
    """Get all configuration as a dictionary"""
    return {
        'base_url': base_url,
        'headless': headless_mode,
        'browser': browser_name,
        'slow_mo': slow_mo
    }