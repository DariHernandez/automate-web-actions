#! python3

import pprint, time
from web_scraping import web_automation
from collections import OrderedDict


# ----------------------------- web automation ---------------
# Name of the xlsx file with data, in excel_files folder
file_name = "data base 1.xlsx" 

# Name of the sheet with the information from the xlsx file
sheet_name = "users" 

# True or False. open web Browser en the background
headless = False

# Use the proxy list from proxy_list.txt
proxy = False

# Link of the web page
web_page = "https://www.multipleincomefunnel.com/cp1/winningwithquincy/5email" 

# Empty list for save web actions
web_actions = []

# List of actions in order
web_actions.append (["click", "body > div > div.div-block-5 > a", ""])
time.sleep (5)
web_actions.append (["send_data", "#name", "first name"])
web_actions.append (["send_data", "#email", "email"])
web_actions.append (["click", "body > div > div.popup > div:nth-child(4) > form > input.submit-button-4.w-button", ""])
my_web_automation = web_automation (web_page, headless, web_actions, file_name, sheet_name, proxy)
my_web_automation.make_web_actions ()
my_web_automation.end_browser()
# ------------------------------------------------------------


# ----------------------------- web automation ---------------
# Name of the xlsx file with data, in excel_files folder
file_name = "data base 1.xlsx" 

# Name of the sheet with the information from the xlsx file
sheet_name = "users" 

# True or False. open web Browser en the background
headless = False

# Use the proxy list from proxy_list.txt
proxy = False

# Link of the web page
web_page = "https://app.clickfunnels.com/signupflow" 

# Empty list for save web actions
web_actions = []

# List of actions in order
web_actions.append (["send_data", "#tmp_input-71861 > input", "first name"])
web_actions.append (["send_data", "#input-26998 > input", "email"])
web_actions.append (["send_data", "#input-90660 > input", "pass"])
web_actions.append (["click", "#tmp_button-85505 > a", ""])
my_web_automation = web_automation (web_page, headless, web_actions, file_name, sheet_name, proxy)
my_web_automation.make_web_actions ()
my_web_automation.end_browser()
# ------------------------------------------------------------


# ----------------------------- web automation ---------------
# Name of the xlsx file with data, in excel_files folder
file_name = "data base 1.xlsx" 

# Name of the sheet with the information from the xlsx file
sheet_name = "users" 

# Use the proxy list from proxy_list.txt
proxy = False

# True or False. open web Browser en the background
headless = False

# Link of the web page
web_page = "https://music.musify.it/en/musify-waitinglist/?utm_campaign=blast2million&utm_medium=email&utm_source=blast" 

# Empty list for save web actions
web_actions = []

# List of actions in order
web_actions.append (["send_data", "#form-field-name", "first name"])
web_actions.append (["send_data", "#form-field-email", "email"])
web_actions.append (["click", "#pulsante > span > span.elementor-button-text", ""])
my_web_automation = web_automation (web_page, headless, web_actions, file_name, sheet_name, proxy)
my_web_automation.make_web_actions ()
my_web_automation.end_browser()
# ------------------------------------------------------------


# ----------------------------- web automation ---------------
# Name of the xlsx file with data, in excel_files folder
file_name = "data base 1.xlsx" 

# Name of the sheet with the information from the xlsx file
sheet_name = "users" 

# True or False. open web Browser en the background
headless = False

# Use the proxy list from proxy_list.txt
proxy = False

# Link of the web page
web_page = "https://membership.thehhacademy.com/subscribe" 

# Empty list for save web actions
web_actions = []

# List of actions in order
web_actions.append (["send_data", "#tmp_input-61960-155-151 > input", "first name"])
web_actions.append (["send_data", "#tmp_input-35198-120-133 > input", "email"])
web_actions.append (["click", "#tmp_button-17970-123-122 > a > span.elButtonMain", ""])
my_web_automation = web_automation (web_page, headless, web_actions, file_name, sheet_name, proxy)
my_web_automation.make_web_actions ()
my_web_automation.end_browser()
# ------------------------------------------------------------
