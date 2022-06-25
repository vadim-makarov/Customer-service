import random

from app import bot


# send_results = client.sms.send(to=number, message=message)


def send_sms(number, time=None):
    if time is not None:
        message = f'Dear customer, your service is scheduled for tomorrow at {time}. Please be on time.'
        bot.send_message('326063522',
                         f'Dear customer, your service is scheduled for tomorrow at {time}. Please be on time.')
        # client.sms.send(to=number, message=message)
        return message
    code = str(random.randint(1000, 10000))
    message = f'Your sms verification code is {code}'
    # client.sms.send(to=number, message=message)
    return code


# def reminder():
#     services = Service.query.all()
#     for service in services:
#         if service.service_date.day - datetime.now().date().day == 1:
#             send_sms(number=service.client.phone_number, time=service.service_time)
#             bot.send_message('326063522', f'Remainder for {service.client.username} was sent')
