from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from random import randint

from faker import Faker

fake = Faker(['ru_RU'])


def generate_phone_number() -> str:
    """Генерация номера телефона для тестового пользователя"""
    phone_number = f'+7{randint(9000000000, 9999999999)}'
    return phone_number


@dataclass
class TestService:
    """Describes test service's model"""
    service1: str = field(default='Chicken Burger')
    service2: str = field(default='Pepsi')
    service3: str = field(default='Delivery')
    service_date: str = datetime.today().strftime("%m-%d-%Y")
    service_time: str = field(default='14:00')


@dataclass
class TestReview:
    """Describes test Review model"""
    text: str = field(default_factory=fake.paragraph(nb_sentences=5))


@dataclass
class TestUser:
    """Describes test user's model"""
    username: str = field(default_factory=fake.name)
    phone_number: str = field(default_factory=generate_phone_number)
