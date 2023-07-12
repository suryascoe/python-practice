import smtplib
import datetime as dt
import random

MY_EMAIL = "surya.scoe3154@gmail.com"
MY_PASSWORD = "xvrbzevegflkakzq"
TO_ADDRESS = "suryadon12@gmail.com"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 2:
    with open("quotes.txt", "r") as data:
        quotes = data.readlines()
        quote = random.choice(quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_ADDRESS, msg=f"Subject:Monday Motivation\n\n{quote}")
