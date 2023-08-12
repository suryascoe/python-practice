from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

cookie_obj = driver.find_element(By.ID, "cookie")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5
while True:
    cookie_obj.click()
    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = items_ids[n]

        collected_cookie = driver.find_element(By.ID, "money").text
        if "," in collected_cookie:
            collected_cookie = collected_cookie.replace(",", "")
        cookie_count = int(collected_cookie)

        affordable_upgrade = {}
        for cost, item_id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrade[cost] = item_id

        highest_affordable_upgrade = max(affordable_upgrade)
        print(highest_affordable_upgrade)
        to_purchase_id = affordable_upgrade[highest_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        timeout = time.time() + 5

        if time.time() > five_min:
            cookie_per_s = driver.find_element(By.ID, "cps").text
            print(cookie_per_s)
            break
