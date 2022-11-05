from discord import app_commands, Interaction, Member, Embed
from discord.ext import commands

from ganyuDB import ganyuDB as gdb
from utils import validateUID

class userCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='account', description="Connects your UID to your discord account.")
    async def account(self, i: Interaction, uid: str):
        name = i.user.name + '#' + i.user.discriminator
        pfp = i.user.display_avatar
        
        if uid is None:
            desc = f'Please supply a UID to connect to {name}'
            embed = Embed(description=desc)
            embed.set_author(name='Error', icon_url=pfp.url)
            await i.response.send_message(embed=embed, ephemeral=True)
            return
        
        uidV = await validateUID(uid)

        if not uidV[0]:
            desc = f'**Invalid UID**'
            embed = Embed(description=desc)
            embed.set_author(name='Error', icon_url=pfp.url)
            await i.response.send_message(embed=embed, ephemeral=True)
            return
        
        if not uidV[2]:
            desc = f"**That UID doesn't exist.**"
            embed = Embed(description=desc)
            embed.set_author(name='Error', icon_url=pfp.url)
            await i.response.send_message(embed=embed, ephemeral=True)
            return
        
        e = gdb.createUser(i.user.id, uid)
        match e: # TODO: Rewrite this in a more backwards-compatible way. (Python 3.10)
            case 0:
                desc = f'**Successfully connected your account to {uid}**'
                embed = Embed(description=desc)
                embed.set_author(name='Success', icon_url=pfp.url)
                embed.add_field(name='UID Validation Layers', value=f'**IsValid:** {uidV[0]}\n**Exists:** {uidV[2]}\n**Server Region:** {uidV[1]}\n**Creation Rank:** {uidV[3]}\n')
                await i.response.send_message(embed=embed, ephemeral=True)
            case 1:
                _uid = gdb.getUID(i.user.id)[0]
                desc = f'**There already is a UID connected to your account.** ({_uid})\n\nUse **/account-update** to change it.'
                embed = Embed(description=desc)
                embed.set_author(name='Error', icon_url=pfp.url)
                await i.response.send_message(embed=embed, ephemeral=True)
            case 2:
                _id = int(gdb.getID(uid)[0])
                desc = f'**This UID is already connected to another user.** ({_id=})'
                embed = Embed(description=desc)
                embed.set_author(name='Error', icon_url=pfp.url)
                await i.response.send_message(embed=embed, ephemeral=True)
            
    @app_commands.command(name='account-update', description="Updates the UID connected to your discord account.")
    async def accountUpdate(self, i: Interaction, uid: str):
        name = i.user.name + '#' + i.user.discriminator
        pfp = i.user.display_avatar
        
        if uid is None:
            desc = f'Please supply a UID to connect to {name}'
            embed = Embed(description=desc)
            embed.set_author(name='Error', icon_url=pfp.url)
            await i.response.send_message(embed=embed, ephemeral=True)
            return
        
        uidV = await validateUID(uid)

        if not uidV[0]:
            desc = f'**Invalid UID**'
            embed = Embed(description=desc)
            embed.set_author(name='Error', icon_url=pfp.url)
            await i.response.send_message(embed=embed, ephemeral=True)
            return
        
        if not uidV[2]:
            desc = f"**That UID doesn't exist.**"
            embed = Embed(description=desc)
            embed.set_author(name='Error', icon_url=pfp.url)
            await i.response.send_message(embed=embed, ephemeral=True)
            return

        e = gdb.updateUser(i.user.id, uid)
        match e: # TODO: Rewrite this in a more backwards-compatible way. (Python 3.10)
            case 0:
                desc = f'**Successfully updated your UID to {uid}.**'
                embed = Embed(description=desc)
                embed.set_author(name='Success', icon_url=pfp.url)
                embed.add_field(name='UID Validation Layers', value=f'**IsValid:** {uidV[0]}\n**Exists:** {uidV[2]}\n**Server Region:** {uidV[1]}\n**Creation Rank:** {uidV[3]}\n')
                await i.response.send_message(embed=embed, ephemeral=True)
            case 2:
                _id = int(gdb.getID(uid)[0])
                desc = f'**This UID is already connected to another user.** ({_id=})'
                embed = Embed(description=desc)
                embed.set_author(name='Error', icon_url=pfp.url)
                await i.response.send_message(embed=embed, ephemeral=True)
            case 3:
                desc = f'**There was an error with the database, try running /account and connecting your account again.**'
                embed = Embed(description=desc)
                embed.set_author(name='Error', icon_url=pfp.url)
                await i.response.send_message(embed=embed, ephemeral=True)
            
    @app_commands.command(name='account-remove', description="Removes your record from the database.")
    async def accountRemove(self, i: Interaction):
        pfp = i.user.display_avatar

        e = gdb.removeUser(i.user.id)
        match e: # TODO: Rewrite this in a more backwards-compatible way. (Python 3.10)
            case 0:
                desc = f'**Successfully removed your UID.**'
                embed = Embed(description=desc)
                embed.set_author(name='Success', icon_url=pfp.url)
                await i.response.send_message(embed=embed, ephemeral=True)
            case 2:
                desc = f'**There are no records to delete.**'
                embed = Embed(description=desc)
                embed.set_author(name='Error', icon_url=pfp.url)
                await i.response.send_message(embed=embed, ephemeral=True)
            case 3:
                desc = f'**There was an error with the database.**'
                embed = Embed(description=desc)
                embed.set_author(name='Error', icon_url=pfp.url)
                await i.response.send_message(embed=embed, ephemeral=True)
                
    @app_commands.command(name='account-add-cookie', description="connects your genshin account cookie to your discord account (optional)")
    async def accountAddCookie(self, i: Interaction, cookie: str = "nocookie"):
        pfp = i.user.display_avatar
        desc = f'**Please be patient, this command should be available soon.**'
        embed = Embed(description=desc)
        embed.set_author(name='Error', icon_url=pfp.url, title='Command not Implemented!')
        await i.response.send_message(embed=embed, ephemeral=True)
        
        # TODO: Pretty self explanatory.

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(userCog(bot))

