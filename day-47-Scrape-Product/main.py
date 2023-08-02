import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

product_url = "https://www.amazon.in/dp/B0C73QLNMV?&linkCode=sl1&tag=tv2023-21&linkId" \
              "=8bca44821f2e9f565ea25681fa3fc6f1&language=en_IN&ref_=as_li_ss_tl"
USERNAME = "Yor Email"
PASSWORD = "Your App Password"

headers = {
    "User-Agent": "Chrome/115.0.0.0",
    "Accept-Language": "en-IN"
}

response = requests.get(url=product_url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")
raw_price = soup.find(name="span", class_="a-price-whole").getText()
price = int(raw_price.replace(",", "").replace(".", ""))

if price < 55499:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=USERNAME, password=PASSWORD)
        connection.sendmail(from_addr=USERNAME, to_addrs="Receivers Email", msg=f"Subject: Amazon Price Drop "
                                                                                     f"Alert\n\nYour product price "
                                                                                     f"has been dropped:\nClick below "
                                                                                     f"link:\n{product_url}")
