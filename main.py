#! python3

import pprint
from excel_read import excel_file
from web_scraping import web_automation
from collections import OrderedDict

# Name of the xlsx file with data, in excel_files folder
file_name = "data base 1.xlsx" 

# Name of the sheet with the information from the xlsx file
sheet_name = "users" 

# True or False. open web Browser en the background
headless = False


# Get data from exel file
my_excel_file = excel_file(file_name)
data = my_excel_file.get_data_sheet(sheet_name)



# ----------------------------- web automation ---------------
# Link of the web page
web_page = "https://music.musify.it/en/musify-waitinglist/?utm_campaign=blast2million&utm_medium=email&utm_source=blast" 

# Empty list for save web actions
web_actions = []

# List of actions in order
web_actions.append (["send_data", "#form-field-name", "first name"])
web_actions.append (["send_data", "#form-field-email", "email"])
web_actions.append (["click", "#pulsante > span > span.elementor-button-text", ""])

my_web_automation = web_automation (web_page, headless, web_actions)
my_web_automation.make_web_actions (data)
# ------------------------------------------------------------

    