import os
from twilio.rest import Client
from random import randrange
from datetime import date



def send_text():
    #List of workout that are ranmdoly texted thorughout the day
    workouts = ['You should do an amount of pushups equal to your age!','You should do an amount of situps equal to your age!',
            'You should run 2 miles!','You should do 25 jumping jacks!', 'You should do 25 Bicep curls!']
    mm = randrange(1,5)
    #add your free twilio account SID and Token as environment variables
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    try:
        client = Client(account_sid, auth_token)
        #change from and to numbers
        message = client.messages.create(body=workouts[int(mm)],from_='twilio_number',to='your_number')
        print('Message sent!...')
    except:
        print('Could not send text!...')

send_text()