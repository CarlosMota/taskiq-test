import asyncio
import logging

from app import main

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)-15s - %(levelname)-8s - %(message)s'
)

asyncio.run(main())