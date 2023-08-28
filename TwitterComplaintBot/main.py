from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

PROMISED_DOWN = 10
PROMISED_UP = 5
X_EMAIL = "YOUR EMAIL"
X_PASSWORD = "YOUR PASSWORD"
SPEEDTEST_ADDRESS = "https://www.speedtest.net/"
X_URL = "https://twitter.com/i/flow/login"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(url=SPEEDTEST_ADDRESS)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get(url=X_URL)
        self.driver.maximize_window()
        time.sleep(5)
        username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        username.send_keys(X_EMAIL)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
        time.sleep(5)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]')
        password.send_keys(X_PASSWORD)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
        time.sleep(10)
        #For Post


IST = InternetSpeedTwitterBot()
IST.get_internet_speed()
print(f"down: {IST.down}\nup: {IST.up}")
IST.tweet_at_provider()
