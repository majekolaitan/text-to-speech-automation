from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

username_id = 'loginemail'
password_id = 'loginpassword'
submit_button_id = 'login_button'

your_username = 'enter_your_email'
your_password = 'enter_your_password'

# Open the webpage
driver.get("https://app.blasteronline.com/user/login")

time.sleep(2)

driver.find_element(By.ID, username_id).send_keys(your_username)
driver.find_element(By.ID, password_id).send_keys(your_password)

time.sleep(20)

# Find all <a> elements
link_elements = driver.find_elements_by_xpath("//td/a")

# Extract href attributes from each <a> element
href_values = [link.get_attribute("href") for link in link_elements]

# Print the extracted href values
for href in href_values:
    print(href)

# Close the browser
driver.quit()
