from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

SIMILAR_ACCOUNT = ""
USERNAME = "YOUR USERNAME"
PASSWORD = "YOUR PASSWORD"
INSTA_URL = "https://www.instagram.com/accounts/login/"



class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def login(self):
        is_login_successfull = False
        self.driver.get(url=INSTA_URL)
        self.driver.maximize_window()
        time.sleep(5)
        # As my Account Connected to FB, so I am Login through that
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[5]/button/span[2]').click()
        time.sleep(3)
        # Login on FB
        username = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH, '//*[@id="pass"]')
        password.send_keys(PASSWORD)
        self.driver.find_element(By.XPATH, '//*[@id="loginbutton"]').click()
        time.sleep(5)
        while not is_login_successfull:
            try:
                self.driver.find_element(By.NAME, 'Home')
                is_login_successfull = True
            except Exception:
                print("Waiting for 10 sec, to let user login.")
                time.sleep(10)

    def find_followers(self):
        pass

    def follow(self):
        pass


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
