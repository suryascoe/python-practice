##################### Hard Starting Project ######################
from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "Your_Email"
MY_PASSWORD = "Your_App_Password"
TO_ADDRESS = "Receiver_Email"


today = (datetime.now().month, datetime.now().day)

birthdays_df = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in birthdays_df.iterrows()}


if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as data:
        contents = data.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_ADDRESS, msg=f"Subject: Happy Birthday\n\n{contents}")

