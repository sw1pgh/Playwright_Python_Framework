import pytest
from playwright.sync_api import sync_playwright


# Global Control for headless or headed. Remember to keep it True before 'master' push
# True: headless
# Fale: headed
mode = True

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as launcher:
        yield launcher

@pytest.fixture(scope="class", params=["chromium" , "firefox", "webkit"])
def browser_context(playwright_instance, request):

    browser = getattr(playwright_instance, request.param).launch(
        headless=mode, args=["--start-maximized"]
    )
    context = browser.new_context()

    yield context

    context.close()
    browser.close()


@pytest.fixture(scope="class")
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()