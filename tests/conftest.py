from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

@pytest.fixture
def user_data() -> Dict[str, str]:
    """
    Session-scoped fixture - same user data for all tests in the test session.
    Useful when you want to use the same user across multiple tests.
    """
    first_name = "Test"
    last_name = "User"
    
    # Generate unique email once per test session
    number = random.randrange(1000, 9999)
    email = f"{first_name[0].lower()}{last_name[:3].lower()}{number}@gmail.com"
    
    return {
        "firstname": first_name,
        "lastname": last_name,
        "email": email,
        "password": "malli123",
        "birthday": "1981/10/10",
        "profileimage": "00a075fb-dc86-4b6a-bfd9-d092273a81e9.jpg",
    }


@pytest.fixture(scope="session")
def playwright():
    """Fixture to manage Playwright instance."""
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    """Fixture to manage browser instance."""
    if not force_new_browser_session:
        logger.info("Launching browser for the session...")
        browser = getattr(playwright, browser_name).launch(headless=headless_mode)
        yield browser
        logger.info("Closing browser after the session...")
        browser.close()
    else:
        logger.info("No browser launched for the session (force_new_browser_session=True).")
        yield None

@pytest.fixture(scope="session")
def browser_context(browser, playwright):
    """Fixture to manage browser context."""
    if not force_new_browser_session:
        logger.info("Creating a new browser context for the session...")
        context = browser.new_context()
        yield context
        logger.info("Closing browser context after the session...")
        context.close()
    else:
        logger.info("No browser context created for the session (force_new_browser_session=True).")
        yield None

@pytest.fixture
def page(browser_context, playwright):
    """Fixture to manage page instance."""
    if force_new_browser_session:
        logger.info("Launching new browser and context for this test case...")
        browser = getattr(playwright, browser_name).launch(headless=headless_mode)
        context = browser.new_context()
        page = context.new_page()

        yield page
        logger.info("Closing browser and context for this test case...")
        context.close()
        browser.close()
    else:
        logger.info("Reusing browser context and creating a new page for this test case...")
        page = browser_context.new_page()
        yield page
        logger.info("Closing page for this test case...")
        page.close()
