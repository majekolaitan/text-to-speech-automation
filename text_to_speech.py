import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import re

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

language_selector  = driver.find_element(By.ID, 'select2-ttp-language-container')
language_selector.click()
time.sleep(2)
# language_select  = driver.find_element(By.ID, 'select2-ttp-language-result-63de-en-CA')
# language_select.click()
focused_element = driver.switch_to.active_element
focused_element.send_keys("Canada")
time.sleep(1)
focused_element.send_keys(Keys.ENTER)
time.sleep(2)
voice_element = driver.find_element(By.ID, 'ttsVoiceDiven-CA-ClaraNeural')
voice_element.click()

time.sleep(2)

input_folder = 'output'

# Get sorted list of file names from input folder with custom sorting key
file_names = sorted(os.listdir(input_folder), key=lambda x: int(re.search(r'(\d+)', x).group(1)))

for file_name in file_names:
    file_path = os.path.join(input_folder, file_name)
    with open(file_path, 'r') as file:
        text_content = file.read()
    
    # Find the text area and submit button elements
    text_area = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "tts-tarea")))
    submit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "ttsGenerateBtn")))
    
    # Paste the content of the file into the text area
    text_area.clear()
    time.sleep(2)

    driver.execute_script("document.getElementById('tts-tarea').value = arguments[0];", text_content)
    time.sleep(0.2)
    text_area.send_keys(" ")
    
    time.sleep(2)

    # Click the submit button
    submit_button.click()

    time.sleep(5)

    # Check if there is a popup with id "oktogenerate" and click it if present
    try:
        confirm_selector = "button.swal2-confirm.btn.btn-danger.emo-cancel-btn.mr-10"
        confirm_popup = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, confirm_selector)))
        confirm_popup.click()
    except:
        pass

    time.sleep(10)

    # Check if there is a popup with okay button and click it if present
    try:
        okay_selector = "button.swal2-confirm.swal2-styled"
        okay_selector_popup = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, okay_selector)))
        okay_selector_popup.click()
    except:
        pass
    
    # Wait for 20 seconds
    time.sleep(2)
    
    # Wait for the text area and submit button to be visible again
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "tts-tarea")))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "ttsGenerateBtn")))

driver.quit()
