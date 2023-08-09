from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://secure-retreat-92358.herokuapp.com/")
# Enter First Name
f_name = driver.find_element(By.NAME, "fName")
f_name.send_keys("Test")

# Enter Last Name
l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys("Singh")

# Enter Email Address
email = driver.find_element(By.NAME, "email")
email.send_keys("test.singh@xyz.com")

# Click Sign Up Button
btn_signup = driver.find_element(By.CSS_SELECTOR, "form button")
btn_signup.click()


