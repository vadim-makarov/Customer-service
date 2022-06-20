from datetime import datetime

from smsapi.client import SmsApiPlClient

import app
from app.models import Service

client = SmsApiPlClient(access_token=app.Config.SMS_TOKEN)
# send_results = client.sms.send(to=number, message=message)

import random


def send_sms(number, time=None):
    if time is not None:
        message = f'Dear customer, your service is scheduled for tomorrow at {time}. Please be on time.'
        # client.sms.send(to=number, message=message)
        return message
    code = str(random.randint(1000, 10000))
    message = f'Your sms verification code is {code}'
    # client.sms.send(to=number, message=message)
    return code


def reminder():
    services = Service.query.all()
    for service in services:
        if service.service_date.day - datetime.now().date().day == 1:
            # send_sms(number=service.client.phone_number, time=service.service_time)
            f'Remainder for {service.client.username} was sended'

