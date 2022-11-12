import asyncio
import logging
import math

from discord.ext import commands

__all__ = ('TheHTTPBot',)

log = logging.getLogger(__name__)


class TheHTTPBot(commands.Bot):
    extension_list = [
        '.commands'
    ]

    def __init__(self, *args, sync_on_start: bool, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.sync_on_start = sync_on_start

    async def prepare(self) -> None:
        log.info('Loading %d extension(s)', len(self.extension_list))
        for ext in self.extension_list:
            await self.load_extension(ext, package=__name__)

        if self.sync_on_start:
            log.info('Synchronizing application commands')
            await self.tree.sync()

    async def serve(self, token: str) -> None:
        """Login without a gateway connection and serve the bot indefinitely."""
        async with self:
            await self.prepare()
            await self.login(token)
            await asyncio.sleep(math.inf)
