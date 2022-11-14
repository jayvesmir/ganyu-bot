from discord import app_commands, Interaction, Embed
from discord.ext import commands

from ganyuDB import ganyuDB as gdb

class genshinCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(genshinCog(bot))
