import logging
from taskiq_aio_pika import AioPikaBroker
from taskiq.schedule_sources import LabelScheduleSource
from taskiq import TaskiqScheduler, TaskiqEvents, TaskiqState

broker = AioPikaBroker(
    "amqp://admin:admin@localhost:5672/",
    queue_name="taskiq_queue",
    exchange_name="taskiq_exchange",
)

import tasks

# Fonte de agendamento (substituindo o RedisScheduleSource)
# Note: Para RabbitMQ, você pode usar o LabelScheduleSource ou implementar um custom source
scheduler = TaskiqScheduler(
    broker,
    sources=[
        LabelScheduleSource(broker),  # Para tarefas agendadas via decorators
        # Adicione aqui outras fontes de agendamento se necessário
    ]
)

@broker.on_event(TaskiqEvents.WORKER_STARTUP)
async def startup(state: TaskiqState) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)-15s - %(levelname)-8s - %(message)s'
    )
    logger = logging.getLogger(__name__)
    logger.info("Starting scheduler...")

    state.logger = logger


@broker.on_event(TaskiqEvents.WORKER_SHUTDOWN)
async def shutdown(state: TaskiqState) -> None:
    state.logger.info("Scheduler stopped")