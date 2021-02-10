#!python3

import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from excel_read import excel_file
from proxy import get_random_proxy

class web_automation (): 
    """
    Class to make web automation
    """

    def __init__ (self, web_page, headless, web_actions, file_name, sheet_name, proxy): 
        """
        Constructor of class
        """

        logging.disable()

        # Run a loop to find a functional proxy
        while True: 
            try: 
                # Get proxy
                self.proxy = get_random_proxy()

                # Variables for class
                self.__web_page = web_page
                self.__headless = headless
                self.__web_actions = web_actions

                self.__browser = self.__get_chrome_instance()
                self.__browser.set_page_load_timeout (10)

                if proxy: 
                    print ("Loading page: {}\nProxy: {}".format(self.__web_page, self.proxy))

                # Load page
                self.__browser.get (self.__web_page)

                # Verify the correct load of the page
                try: 
                    self.__browser.find_element_by_css_selector("#reload-button")
                except: 
                    break
                else:
                    print ("Page take a lot of time to load. Trying again.")
                    raise TimeoutError ("Page take a lot of time to load. Trying again.")

            except: 
                continue
            else: 
                break


        # Get data from exel file
        my_excel_file = excel_file(file_name)
        self.data = my_excel_file.get_data_sheet(sheet_name)


    def __get_chrome_instance (self):
        """
        Return an instance of google chrome browser
        """

        options = webdriver.ChromeOptions()

        if self.__headless == True: 
            options.add_argument("--headless")

        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')  
        options.add_argument('--start-maximized')
        options.add_argument('--proxy-server={}'.format(self.proxy))

        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        return browser

    def __send_data (self, selector, data): 
        """
        Send data to specific input fill
        """
        print ("\t - sending information to input fill")
        elem = self.__browser.find_element_by_css_selector (selector)
        elem.send_keys (data)

    def __click (self, selector): 
        """
        Send data to specific input fill
        """
        print ("\t - clicking an element")
        elem = self.__browser.find_element_by_css_selector (selector)
        elem.click()

    def make_web_actions (self): 
        """
        Loadf page and make actions in the web page (clicks and send data), with specific data structure
        """

        print ("Processing actions on the web page: ")

        # Loop for each in data from excel sheet
        for data_row in self.data:

            # Print current row for the loop
            column = list(data_row.keys()) [0]
            print ("Current row: ", data_row[column])


            # Make action in browser
            for action_data in self.__web_actions: 

                action_name = action_data[0]
                selector = action_data[1] 

                if action_name == "send_data":
                    data_to_send = data_row[action_data[2]]
                    self.__send_data (selector, data_to_send)
                elif action_name == "click": 
                    self.__click (selector)
            
            # End process in each loop
            self.__reload_browser()

    def end_browser (self):
        """
        Close the current instance of chrome
        """

        self.__browser.close()

    def __reload_browser (self): 
        """
        Close the current instance of the web browser and reload in the same page
        """

        self.end_browser()
        self.__browser = self.__get_chrome_instance()
        print ("Loading page")
        self.__browser.get (self.__web_page)

