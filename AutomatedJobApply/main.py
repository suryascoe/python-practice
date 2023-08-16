from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = "Your Account Email"
ACCOUNT_PASSWORD = "Your Account Password"
FILTERED_URL = "https://www.linkedin.com/jobs/search/?currentJobId=3690532380&f_E=4&f_JT=F&f_WT=2&geoId=102713980" \
               "&keywords=automation%20engineer&location=India&refresh=true"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(url=FILTERED_URL)
driver.maximize_window()
time.sleep(3)

# Get to Sing In Page
driver.find_element(By.CSS_SELECTOR, "nav div a.nav__button-secondary.btn-md.btn-secondary-emphasis").click()

time.sleep(2)
# Log into the Account
username = driver.find_element(By.ID, "username")
username.send_keys(ACCOUNT_EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(ACCOUNT_PASSWORD)
password.send_keys(Keys.ENTER)
# driver.find_element(By.CSS_SELECTOR, "form div.login__form_action_container button").click()

time.sleep(3)


jobs_list = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")


for job in jobs_list:
    job.click()
    time.sleep(3)
    save_button = driver.find_element(By.CSS_SELECTOR, '.jobs-save-button')
    if "Saved" not in save_button.text:
        save_button.click()

