import asyncio
from dataclasses import dataclass
import logging
import tomllib

import uvicorn

from ..bot import TheHTTPBot

__all__ = ('TheHTTPApp', 'TheHTTPConfig', 'TheHTTPCredentials')

log = logging.getLogger(__name__)


@dataclass
class TheHTTPConfig:
    """Defines all configuration options for the app."""

    sync_on_start: bool
    """Toggles application command synchronization on startup."""

    @classmethod
    def from_file(cls, toml_path: str) -> "TheHTTPConfig":
        """Loads the configuration from a TOML file."""
        with open(toml_path, 'rb') as f:
            data = tomllib.load(f)

        return cls(
            sync_on_start=data['bot']['sync_on_start'],
        )


@dataclass
class TheHTTPCredentials:
    """Defines any credentials required by the app."""

    bot_token: str
    """The token used to authenticate with the discord API."""


class TheHTTPApp:
    def __init__(self, config: TheHTTPConfig) -> None:
        self.config = config
        self.bot: TheHTTPBot | None = None
        self.server: uvicorn.Server | None = None
        self.bot_task: asyncio.Task | None = None
        self.server_task: asyncio.Task | None = None

    async def start(self, credentials: TheHTTPCredentials):
        self.bot = bot = TheHTTPBot(
            sync_on_start=self.config.sync_on_start
        )

        server_config = uvicorn.Config(
            '..server:app',
            # TODO figure out other uvicorn options
        )
        self.server = server = uvicorn.Server(server_config)

        async with asyncio.TaskGroup() as tg:
            self.bot_task = tg.create_task(bot.serve(credentials.bot_token))
            self.server_task = tg.create_task(server.serve())
