from twilio.rest import Client
from decouple import config


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.account_sid = config("TWILIO_ACCOUNT_SID")
        self.auth_token = config("TWILIO_AUTH_TOKEN")
        self.TWILIO_NUMBER = config("TWILIO_NUMBER")
        self.MY_NUMBER = config("MY_NUMBER")
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self, body: str) -> None:
        message = self.client.messages.create(
            from_=self.TWILIO_NUMBER,
            body=body,
            to=self.MY_NUMBER,
        )
        print(message.sid)
