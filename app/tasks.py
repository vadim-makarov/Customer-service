"""Example of adding tasks on app startup."""
from datetime import datetime

from . import bot
from .extensions import scheduler
from .models import Service
from .sms import send_sms


@scheduler.task(
    "interval",
    id="reminder",
    seconds=30,
    max_instances=1,
    start_date="2022-06-26 01:43:00",
)
def reminder():
    with scheduler.app.app_context():
        services = Service.query.all()
        for service in services:
            if service.service_date.day - datetime.now().date().day == 1:
                send_sms(number=service.client.phone_number, time=service.service_time)
                bot.send_message('326063522', f'Remainder for {service.client.username} was sent')
                print("running task 1!")
                with scheduler.app.app_context():
                    print(scheduler.app.config)
