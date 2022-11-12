import asyncio
import logging
import math
import os

import discord
from discord.ext import commands

__all__ = ('TheHTTPBot',)

INVITE_PERMISSIONS = discord.Permissions(
    add_reactions=True,
    attach_files=True,
    change_nickname=True,
    embed_links=True,
    read_message_history=True,
    read_messages=True,
    send_messages=True,
    send_messages_in_threads=True,
    use_external_emojis=True,
)

log = logging.getLogger(__name__)


class TheHTTPBot(commands.Bot):
    extension_list = [
        '.commands'
    ]

    def __init__(self, *args, sync_on_start: bool, **kwargs) -> None:
        super().__init__(
            *args,
            command_prefix='!',
            intents=discord.Intents.none(),
            **kwargs
        )
        self.sync_on_start = sync_on_start
        self.running_task: asyncio.Task | None = None

    async def serve(self) -> None:
        """Login without a gateway connection and serve the bot indefinitely."""
        async with self:
            log.info('Loading %d extension(s)', len(self.extension_list))
            for ext in self.extension_list:
                await self.load_extension(ext, package=__name__)

            log.info('Authenticating with the Discord API')
            await self.login(os.getenv('BOT_TOKEN'))

            if self.sync_on_start:
                log.info('Synchronizing application commands')
                await self.tree.sync()

            invite = discord.utils.oauth_url(
                self.application.id,
                permissions=INVITE_PERMISSIONS,
            )
            logging.info('Invite this bot using the following link: %s', invite)

            await asyncio.sleep(math.inf)

    def start_serving(self) -> None:
        if self.running_task is not None:
            raise RuntimeError('Bot is already being served')
        self.running_task = asyncio.create_task(self.serve())

    def stop_serving(self) -> None:
        if self.running_task is None:
            raise RuntimeError('Bot has not yet been served or has stopped serving')
        self.running_task.cancel()
        self.running_task = None
