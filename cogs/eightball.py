from discord import app_commands, Interaction
from discord.ext import commands

import random

class eightballCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='eightball', description='Rolls the 8ball.')
    async def eightball(interaction: Interaction, query: str):
        responses = ['It is certain.',"It is decidedly so.","Without a doubt.","Yes definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]
        await interaction.response.send_message(f'**Question:** {query}\n**Answer:** {random.choice(responses)}')

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(eightballCog(bot))