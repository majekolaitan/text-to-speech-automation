from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import requests

driver = webdriver.Chrome()

username_id = 'loginemail'
password_id = 'loginpassword'
submit_button_id = 'login_button'

your_username = 'enter_your_email'
your_password = 'enter_your_password'

# Function to download file
def download_file(url, folder):
    local_filename = os.path.join(folder, url.split('/')[-1])
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    return local_filename

# Open the webpage
driver.get("https://app.blasteronline.com/user/login")

time.sleep(2)

driver.find_element(By.ID, username_id).send_keys(your_username)
driver.find_element(By.ID, password_id).send_keys(your_password)

time.sleep(20)

# Find all <a> elements
elements = driver.find_elements(By.CSS_SELECTOR, "#blastered_datatable > tbody > tr > td:nth-child(7) > a")

# Create a folder to save the downloaded files if it doesn't exist
download_folder = 'downloads'
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Extract href attributes from each element
hrefs = [element.get_attribute("href") for element in elements]

# Download each file
for element in elements:
    href = element.get_attribute("href")
    if href.endswith('.mp3'):
        filename = download_file(href, download_folder)
        print("Downloaded:", filename)

# Close the WebDriver
driver.quit()
