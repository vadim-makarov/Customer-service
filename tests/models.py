from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime
from random import randint

from faker import Faker

fake = Faker()


def generate_phone_number() -> str:
    """Генерация номера телефона для тестового пользователя"""
    phone_number = f'+7{randint(9000000000, 9999999999)}'
    return phone_number


@dataclass
class NewUser:
    """Describes test user's model"""
    id: int = 1
    username: str = field(default_factory=fake.name)
    phone_number: str = field(default_factory=generate_phone_number)

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}


@dataclass
class NewService(NewUser):
    """Describes test service's model"""

    service1: str = field(default='Chicken Burger')
    service2: str = field(default='Pepsi')
    service3: str = field(default='Delivery')
    service_date: datetime = datetime.today()
    service_time: str = field(default='14:00')


@dataclass
class NewReview(NewUser):
    """Describes test review's model"""
    text: str = field(default_factory=fake.paragraph)
