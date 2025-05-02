
import asyncio
import logging

from taskiq_broker import broker
from tasks import periodic_task, simple_task


logger = logging.getLogger(__name__)

async def main():
    logger.info("Starting the application...")

    logger.info("Starting broker...")
    try:
        await broker.startup()
        task = await periodic_task.kiq()
        print(f"Task sent with ID: {task.task_id}")
    finally:
        # Clean up
        logger.info("Stop broker...")
        await broker.shutdown()


asyncio.run(main())
        