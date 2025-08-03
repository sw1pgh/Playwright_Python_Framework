from playwright.sync_api import Page

class Google_HomePage_Locators:
    def __init__(self, page: Page):
        self.page = page
        self.google_image = page.locator("//*[name()='path' and contains(@d,'M115.75 47')]")