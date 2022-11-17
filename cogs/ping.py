from discord import app_commands, Interaction, Object
from discord.ext import commands

from config import IS_DEBUG, DEBUG_GUILD
DEBUG_GUILD = Object(DEBUG_GUILD)

class pingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='ping', description='Check if the bot lives.', )
    @app_commands.guilds(DEBUG_GUILD if IS_DEBUG else None)
    async def ping(self, i: Interaction):
        await i.response.send_message(f'Pong! ({self.bot.latency*1000:.2f}ms)')

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(pingCog(bot))
    