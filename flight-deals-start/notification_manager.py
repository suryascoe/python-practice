from twilio.rest import Client
import smtplib

TWILIO_ACCOUNT_SID = 'ACd0086696efce5ec5ae71e1e67602a5171'
TWILIO_AUTH_TOKEN = 'ae7177411404aa3675705cc8985d08761'
TWILIO_FROM_NUMBER = '+15736811212154664'
TWILIO_TO_NUMBER = '+917021912122150921'
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "surya.scoe3154@gmail.com"
MY_PASSWORD = "wveroqsqfybvdivlq"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            from_=TWILIO_FROM_NUMBER,
            to=TWILIO_TO_NUMBER,
            body=message
        )

    def send_emails(self, emails, message):
        with smtplib.SMTP(host=MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=email,
                                    msg=f"Subject: New Low Price Flight!\n\n{message}".encode("utf-8"))
