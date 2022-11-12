import logging

import discord

from .app import *
from .bot import *
from . import server


def setup_logging():
    discord.utils.setup_logging()
    log = logging.getLogger(__name__)
    # TODO share handler with discord.py
