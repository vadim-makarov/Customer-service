import random
from datetime import datetime

from app import bot
from app import scheduler
# send_results = client.sms.send(to=number, message=message)
from app.models import Service


def send_sms(number, name=None, time=None):
    if time is not None and name is not None:
        message = f'Dear {name}, your service is scheduled for tomorrow at {time}. Please be on time.'
        bot.send_message('326063522', message)
        # client.sms.send(to=number, message=message)
        return message
    code = str(random.randint(1000, 10000))
    message = f'Your sms verification code is {code}'
    # client.sms.send(to=number, message=message)
    return code


@scheduler.task(
    "interval",
    id="reminder",
    seconds=86400,
    start_date="2022-06-26 19:02:22"
)
def reminder():
    with scheduler.app.app_context():
        services = Service.query.all()
        for service in services:
            if service.service_date.day - datetime.now().date().day == 1:
                send_sms(service.app.phone_number, service.app.username, service.service_time)
