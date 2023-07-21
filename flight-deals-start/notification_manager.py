from twilio.rest import Client
from flight_data import FlightData

TWILIO_ACCOUNT_SID = 'ACd0086696efce5ec5ae71e1e67602a517'
TWILIO_AUTH_TOKEN = 'd1b7e32cb7ce2fefd769c822f66a3406'
TWILIO_FROM_NUMBER = '+15736854664'
TWILIO_TO_NUMBER = '+917021950921'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            from_=TWILIO_FROM_NUMBER,
            to=TWILIO_TO_NUMBER,
            body=message
        )
