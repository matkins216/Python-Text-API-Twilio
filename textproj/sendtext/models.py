from django.db import models
from twilio.rest import Client
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()

# Create your models here.

class Score(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
        if self.result < 11:
            account_sid=env('TWILIO_ACCOUNT_SID')
            auth_token=env('TWILIO_AUTH_TOKEN')
            print(env('TWILIO_ACCOUNT_SID'))
            print(env('TWILIO_AUTH_TOKEN'))
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body='McAvoy or Stewart? These timelines can get so confusing.',
                from_='+13393304638',
                status_callback='http://postb.in/1234abcd',
                to='+17204721204'
                )

            print(message.sid)
        return super().save(*args, **kwargs)