from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# chrome_driver_path = "C:\\Users\\suryasingh04\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Amazon
# driver.get("https://www.amazon.in/dp/B0C73QLNMV?linkCode=sl1&tag=tv2023-21&linkId=8bca44821f2e9f565ea25681fa3fc6f1&language=en_IN&ref_=as_li_ss_tl&th=1")
# price = driver.find_element(By.CLASS_NAME, "a-price-whole").get_attribute(name="innerText")
# print(price)

# PyOrg
driver.get("https://www.python.org/")
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)


