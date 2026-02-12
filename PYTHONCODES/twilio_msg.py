from twilio.rest import Client
from decouple import config

account_sid = config("TWILIO_ACCOUNT_SID")
auth_token = config("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = config("TWILIO_NUMBER")
MY_NUMBER = config("MY_NUMBER")
client = Client(account_sid, auth_token)
my_number = config("MY_NUMBER")


def send_message(body: str) -> None:
    message = client.messages.create(
        from_=TWILIO_NUMBER,
        body=body,
        to=MY_NUMBER,
    )
    print(message.sid)
