# Email automation

# Description
System for auto fil from to specific web page.
Use web scraping with Selenium to make the "actions", and send information from excel spread sheet.
Each instance of chrome update the vpn service of *potonvpn*

# Requirements

### Install python 3.7
1. Delete other python version on your windows system from the control panel
2. Download the executable installer in [this link] (https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe)
3. Follow the installer
    1. Add python 3.7 to path
    2. Customize installation
    3. Optional features: mark all checkboxes
    4. Advances options: install for all users
    5. Install
    6. Close

## Modules:
* selenium
* webdriver_manager
* openpyxl

## Install modules with pip

Open a terminal / cmd window, and run this commands:

```bash
$ pip install selenium
$ pip install webdriver-manager
$ pip install openpyxl
```

# How to use
## Files
* **main.py:** This module have all necessary code to run the project for specific web pages
* **excel_read.py:** module for extact information from xlsx file
* **web_scraping.py:** module for make the web browser automation

## Web automation block
Each block of code, in main file, with the next format, is for automate a specific web page

```python
# ----------------------------- web automation ---------------
file_name = "data base 1.xlsx"

sheet_name = "users"

headless = False

web_page = "https://www.multipleincomefunnel.com/cp1/winningwithquincy/5email"

web_actions = []

...

my_web_automation.make_web_actions ()
my_web_automation.end_browser ()
# ------------------------------------------------- -----------

```

## Variables to modify
* **file_name**: The name of the xlsx file. All xlsx files need to be inside the "excel_files" folder.
* **sheet_name**: Specific sheet inside the file, with the information. You would use one file with many sheets or many files with one sheet.
* **sheet_name**: If this variable is "True", the browser will run in background (whithout visible window), else, chrome will open normally.
* **web_page**: Full address for the web site to make web automation.

## Web actions
Each one of web actions, is a specific **function to make in the browser**.
Example:

```python
web_actions.append (["send_data", "#name", "first name"])
```

The web actions have the structure:
```python
web_actions.append ([action, css_selector, data_column])
```

* **action **:"send_data" or "click". As the name implies, they can send information to an element of the page, or click on something respectively.
* **css selector**: Is a selector from css, to indicate a specific element in the web page. [Click here to know how to get a specific selector in google chrome](https://stackoverflow.com/questions/4500572/how-can-i-get-the-css-selector-in-chrome/45078286), or [click here to learn more about css selectors](https://www.w3schools.com/cssref/css_selectors.asp)
* **data_column**: The name of the spreadsheet column, whose content will be written in the text field. **Only fill in case of "data_send", if a "click" is used, leave as empty string ("")**.