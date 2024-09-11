import datetime
import json
from selenium import webdriver
import time

# Global variable for storing the contact element
contact_element = None 

# Function to generate a birthday greeting message
def generate_birthday_message(contact_name):
    return "Happy Birthday, " + contact_name.split(" ")[0] + "!!"

# Function to retrieve a list of contact names with birthdays on the current date
def find_birthdays_in_json(file, return_attr, month_attr, day_attr, month_value, day_value):
    # Load the JSON data from the file
    data = json.load(file)
    birthday_contacts = []

    # Check each contact for matching birthday month and day
    for contact in data:
        if contact[month_attr] == month_value and contact[day_attr] == day_value:
            birthday_contacts.append(contact[return_attr])
    return birthday_contacts

# Open the JSON file containing birthdays in read-only mode
with open("birthdays.json", "r") as data_file:
    birthday_list = []
    print("Script is running...")

    # Continuously check for contacts with birthdays until found
    while True:
        try:
            # Get the current date
            current_date = datetime.datetime.now()
            birthday_list = find_birthdays_in_json(data_file, "name", "birth_month", "birth_date",
                                                    str(current_date.month), str(current_date.day))
        except json.decoder.JSONDecodeError:
            continue
        if birthday_list:
            break

# Set up Chrome options for the WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=<LOCATION TO YOUR CHROME USER DATA>")

# Create a Chrome WebDriver instance
driver = webdriver.Chrome(executable_path="<LOCATION TO CHROME WEBDRIVER>", options=chrome_options)
driver.get("https://web.whatsapp.com/")

# Wait for the WhatsApp Web page to fully load
time.sleep(10)

print("Contacts with birthdays today:", birthday_list)

# Iterate over the list of birthday contacts
for contact in birthday_list:
    try:
        # Locate the chat element for the contact
        contact_element = driver.find_element_by_xpath('//span[@title ="{}"]'.format(contact))
    except Exception as e:
        print("Error locating contact:", e)
        continue
    
    # Simulate a click on the contact's chat
    contact_element.click()

    while True:
        # Find the chat input box
        message_input = driver.find_element_by_class_name("_13mgZ")
        # Send the birthday greeting message
        message_input.send_keys(generate_birthday_message(contact))
        # Find the send button
        send_button = driver.find_element_by_class_name("_3M-N-")
        # Simulate a click on the send button
        send_button.click()
        break