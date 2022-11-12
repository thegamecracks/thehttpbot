import logging

import discord
import dotenv
from fastapi import FastAPI, Request, status
from fastapi.responses import Response

from .bot import TheHTTPBot
from .config import TheHTTPConfig
from .models import Interaction

CONFIG_PATH = 'config.toml'

# Configuration

dotenv.load_dotenv()
config = TheHTTPConfig.from_file(CONFIG_PATH)

# Logging

discord.utils.setup_logging(level=config.logging_level)
discord_logger = logging.getLogger('discord')

log = logging.getLogger(__name__)
log.setLevel(config.logging_level)
for handler in discord_logger.handlers:
    log.addHandler(handler)

# App

bot = TheHTTPBot(sync_on_start=config.sync_on_start)
app = FastAPI(
    on_startup=[bot.start_serving],
    on_shutdown=[bot.stop_serving],
)


@app.middleware("http")
async def has_logged_in(request: Request, call_next):
    if bot.user is None:
        return Response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content='Not authenticated with the Discord API'
        )
    return await call_next(request)


@app.middleware("http")
async def check_signature(request: Request, call_next):
    # TODO signature checking
    return await call_next(request)


@app.post('/interactions')
async def post_interactions(interaction: Interaction):
    if interaction.type == 1:
        return {'type': 1}

    # TODO dispatch interaction
