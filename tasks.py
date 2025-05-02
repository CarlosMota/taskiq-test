import datetime
import time

from taskiq_broker import broker


@broker.task
async def simple_task():
    print()
    print('Это простая задача без расписания')
    print()


@broker.task(task_name='periodic_task', schedule=[{"cron": "* * * * *"}])
async def periodic_task():
    print()
    print(f"{datetime.datetime.now}: Periodica Task")
    print()


@broker.task
async def dynamic_periodic_task():
    print()
    print(f'{datetime.datetime.now}: Это динамически запланированная периодическая задача')
    print()


@broker.task
async def scheduled_task():
    print()
    print(f'{datetime.datetime.now}: Это запланированная разовая задача')
    print()