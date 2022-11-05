from logger import log
from ganyuDB import ganyuDB as gdb
from utils import validateUID

import re
import discord
from pathlib import Path

from config import TOKEN, PREFIX

from discord.ext import commands
from discord import Member, Client, app_commands
bot: commands.Bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

import random

class Ganyu(commands.Bot):
    def __init__(self):
        super().__init__(intents=discord.Intents.all(), command_prefix=PREFIX)
        self.synced = False

    async def setup_hook(self) -> None:
        for filepath in Path("./cogs").glob('**/*.py'):
            cogName = Path(filepath).stem
            try:
                await self.load_extension(f"cogs.{cogName}")
            except Exception as e:
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
