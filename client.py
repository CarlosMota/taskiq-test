import asyncio
import logging

from tasks import simple_task

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)-15s - %(levelname)-8s - %(message)s'
)


async def main():
    # Envia tarefa para somar números
    task = await simple_task.kiq()
    print(f"Task sent with ID: {task.task_id}")


if __name__ == "__main__":
    asyncio.run(main())