from celery.schedules import crontab

from app import celery, bot


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, tbot_msg, name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(),
        test.s('Happy Mondays!'),
    )


@celery.task()
def tbot_msg():
    bot.send_message('326063522', 'Wanna some Celery?')


@celery.task
def test(arg):
    print(arg)


@celery.task
def add(x, y):
    z = x + y
    print(z)
