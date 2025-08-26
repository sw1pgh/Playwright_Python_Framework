import pytest
from Configurations import constants
from Page_Methods.google_homepage_method import Google_HomePage_Methods

class Test_Google_HomePage_Assertions:
    
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.page = page
        self.homePage_methods = Google_HomePage_Methods(page)
    
    def test_navigation_assertion(self):        
        self.page.wait_for_load_state(constants.loadstate)
        self.homePage_methods.basic_navigation()
        
    def test_google_doodle_navigation(self):
        self.page.wait_for_load_state(constants.loadstate)
        self.homePage_methods.google_doodle_navigation()