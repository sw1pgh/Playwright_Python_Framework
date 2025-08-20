from playwright.sync_api import Page

class Google_HomePage_Locators:
    def __init__(self, page: Page):
        self.page = page
        self.google_image = page.locator("//*[name()='path' and contains(@d,'M115.75 47')]")
        self.feeling_lucky_btn = self.page.locator("div[class='FPdoLc lJ9FBc'] input[name='btnI']")
        self.google_doole_glue_header = self.page.locator("div[id='glue-drawer-2465973'] a[title='Google doodles']")