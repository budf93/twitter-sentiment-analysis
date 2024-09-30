from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Twitter login credentials
username = "nonnegativeint_"
password = "@@#twtenum22"

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open Twitter login page
driver.get("https://twitter.com/login")
driver.implicitly_wait(5)

# Locate the username (or email/phone number) field and enter your username
username_field = driver.find_element(By.NAME, "text")
username_field.send_keys(username)

# Click on the 'Next' button after entering the username
next_button = driver.find_element(By.XPATH, "//span[text()='Next']/..")
next_button.click()

# Wait for the password input to load
time.sleep(3)

# Locate the password field and enter your password
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys(password)

# Click on the 'Log in' button after entering the password
login_button = driver.find_element(By.XPATH, "//span[text()='Log in']/..")
login_button.click()

# Keep the browser open for a few seconds to verify login
time.sleep(10)

# Optionally close the browser after execution
# driver.quit()

