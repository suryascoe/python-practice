from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://tinder.com/")
driver.maximize_window()
time.sleep(5)
# Click Log In.
driver.find_element(By.XPATH, '//*[@id="u-1535117240"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]').click()

time.sleep(10)

# Click on Facebook Log in.
driver.find_element(By.XPATH, '//*[@id="u1031468980"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div').click()

time.sleep(5)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
# print(driver.title)

# Log In to Facebook
# Enter Email
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("YOUR FB EMAIL/NUMBER")
# Enter Password
driver.find_element(By.CSS_SELECTOR, "#pass").send_keys("YOUR FB PASSWORD")
# Click Log In
driver.find_element(By.NAME, "login").click()

time.sleep(20)
driver.switch_to.window(base_window)
print(driver.title)
