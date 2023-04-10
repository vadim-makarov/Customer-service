"""Содержит различные хэлперы"""
import random


def generate_phone_number() -> str:
    """Генерация номера телефона для тестового пользователя"""
    phone_number = f'+7{random.randint(9000000000, 9999999999)}'
    return phone_number


