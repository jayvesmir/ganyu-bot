from discord import app_commands, Interaction, Member, Embed
from discord.ext import commands

class utilityCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='avatar', description="Returns a user's avatar")
    async def avatar(self, i: Interaction, member: Member = None):
        if member is None:
            member = i.user
            
        name = member.name + '#' + member.discriminator
        pfp = member.display_avatar
        color = member.color
        
        embed = Embed(title='Avatar', color=color)
        embed.set_author(name=name, icon_url=pfp.url)
        embed.set_image(url=pfp.url)
        
        await i.response.send_message(embed=embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(utilityCog(bot))

