from pathlib import Path

import discord
from discord.ext import commands
from discord.ext.commands import ExtensionAlreadyLoaded, ExtensionFailed, ExtensionNotLoaded, NoEntryPointError

from logger import log
from config import TOKEN, PREFIX
bot: commands.Bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

class Ganyu(commands.Bot):
    def __init__(self):
        super().__init__(intents=discord.Intents.all(), command_prefix=PREFIX)
        self.synced = False

    async def setup_hook(self) -> None:
        for filepath in Path("./cogs").glob('**/*.py'):
            cogName = Path(filepath).stem
            try:
                await self.load_extension(f"cogs.{cogName}")
            except (ExtensionAlreadyLoaded, ExtensionFailed, ExtensionNotLoaded, NoEntryPointError) as e:
                log('CogLoader').warning(f'Failed to load {cogName}\n {e}')

    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel:
            await channel.send(f'{member.mention} Welcome To The Server!')
              
    async def on_ready(self):
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game('with your data'))
        log().info(f'Ganyu is online as {bot.user}.')

bot = Ganyu()
bot.run(TOKEN)
