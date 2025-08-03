from Configurations import constants
from Page_Objects.google_homepage_locators import Google_HomePage_Locators

class Google_HomePage_Methods:
    
    def __init__(self, page):
        self.page = page
        self.homePage_locators = Google_HomePage_Locators(page)


    def basic_navigation(self):
        page = self.page
        
        with page.expect_navigation(timeout = constants.timeouts):
            self.page.goto(constants.base_URL)
            
        page.wait_for_load_state(constants.loadstate)
    
        assert "google" in self.page.url
        assert self.homePage_locators.google_image.is_visible()