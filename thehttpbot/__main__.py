import asyncio
import os

import dotenv

from . import TheHTTPApp, TheHTTPConfig, TheHTTPCredentials, setup_logging


async def main():
    setup_logging()

    config = TheHTTPConfig.from_file('config.toml')

    dotenv.load_dotenv()
    credentials = TheHTTPCredentials(
        bot_token=os.getenv('BOT_TOKEN'),
    )

    app = TheHTTPApp(config)
    await app.start(credentials)


asyncio.run(main())
