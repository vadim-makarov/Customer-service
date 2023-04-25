"""Contains an SMS generating method"""
import random

from app import bot


def send_sms(number='326063522', name=None, time=None):
    """Generates a sms message if name or time are empty"""
    if time is not None and name is not None:
        message = f'Dear {name}, your service is scheduled for tomorrow at {time}. Please be on time.'
        bot.send_message(number, message)
        return message
    code = str(random.randint(1000, 10000))
    return code
