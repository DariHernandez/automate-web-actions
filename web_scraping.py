#!python3

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class web_automation (): 
    """
    Class to make web automation
    """

    def __init__ (self, web_page, headless, time_out): 
        """
        Constructor of class
        """

        self.web_page = web_page
        self.headless = headless
        self.time_out = time_out

        self.browser = self.__get_chrome_instance()
        self.browser.get (web_page)

    def __get_chrome_instance (self):
        """
        Return an instance of google chrome browser
        """

        options = webdriver.ChromeOptions()

        if self.headless == True: 
            options.add_argument("--headless")

        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')  
        options.add_argument('--start-maximized')

        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        browser.set_page_load_timeout (self.time_out)
        return browser

    def end_browser (self):
        """
        Close the current instance of chrome
        """

        self.browser.close()