from smsapi.client import SmsApiPlClient


token = "bLQCWwiUPawU5xKF4DJE7uZh5lHCrlRjcTwjdXGz"
client = SmsApiPlClient(access_token=token)
# message = "Where is the money, Lebowsky?!"
# number = "+79022516111"
# send_results = client.sms.send(to=number, message=message)

import random


def send_sms(number, message=None):
    if message is None:
        message = random.randint(1000, 10000)
    send_results = client.sms.send(to=number, message=message)
    return message


