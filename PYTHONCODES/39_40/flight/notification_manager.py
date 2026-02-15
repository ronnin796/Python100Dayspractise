from twilio.rest import Client
from decouple import config
import smtplib
from pathlib import Path
import datetime as dt
from typing import Optional


class NotificationManager:
    """
    Handles sending SMS and Email notifications.
    """

    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_PORT = 587

    def __init__(self) -> None:
        # --- Twilio Config ---
        self.account_sid: str = config("TWILIO_ACCOUNT_SID")
        self.auth_token: str = config("TWILIO_AUTH_TOKEN")
        self.twilio_number: str = config("TWILIO_NUMBER")
        self.my_number: str = config("MY_NUMBER")

        self.client = Client(self.account_sid, self.auth_token)

        # --- Email Config ---
        self.email_user: str = config("EMAIL_USER")
        self.email_password: str = config("EMAIL_PASSWORD")
        self.receiver_email: str = config("RECEIVER_EMAIL")

        # --- Other ---
        self.base_dir = Path(__file__).parent
        self.now = dt.datetime.now()

    # =========================
    # SMS
    # =========================
    def send_sms(self, body: str) -> Optional[str]:
        """
        Sends SMS using Twilio.
        Returns message SID if successful.
        """
        try:
            message = self.client.messages.create(
                from_=self.twilio_number,
                body=body,
                to=self.my_number,
            )
            print(f"SMS sent successfully. SID: {message.sid}")
            return message.sid
        except Exception as e:
            print(f"Failed to send SMS: {e}")
            return None

    # =========================
    # EMAIL
    # =========================
    def send_email(self, subject: str, body: str, receiver: str = None) -> None:
        """
        Sends Email using SMTP.
        """
        try:
            with smtplib.SMTP(self.EMAIL_HOST, self.EMAIL_PORT) as connection:
                connection.starttls()
                connection.login(self.email_user, self.email_password)
                connection.sendmail(
                    from_addr=self.email_user,
                    to_addrs=receiver if receiver else self.receiver_email,
                    msg=f"Subject:{subject}\n\n{body}",
                )
            print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send Email: {e}")
