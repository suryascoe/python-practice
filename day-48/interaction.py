from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://en.wikipedia.org/wiki/Main_Page")
articles_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(articles_count.text)
