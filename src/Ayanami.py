import json
from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
TOKEN = json.loads(open('config.json', 'r').read())['token']

import discord
from discord.ext import commands
from discord import Member, app_commands
bot: commands.Bot = commands.Bot(command_prefix="g.", intents=discord.Intents.all())

from logger import log

import random

class Ganyu(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
        
    async def on_ready(self):
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game('with your data'))
        await tree.sync(guild=discord.Object(id=980162247299059792))
        self.synced = True
        log.info(f"Ganyu is online as {bot.user}.")
        
    async def on_member_join(member):
        channel = member.guild.system_channel
        await channel.send(f'{member.mention} Welcome To The Server!')
        
bot = Ganyu()
tree = app_commands.CommandTree(bot)

@tree.command(name='ping', description='Check if the bot lives.', guild=discord.Object(id=980162247299059792))
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! ({bot.latency*1000:.2f}ms)")
    
@tree.command(name='eightball', description='Rolls the 8ball.', guild=discord.Object(id=980162247299059792))
async def self(interaction: discord.Interaction, query: str):
    responses = ["It is certain.","It is decidedly so.","Without a doubt.","Yes definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]
    await interaction.response.send_message(f'**Question:** {query}\n**Answer:** {random.choice(responses)}')
    
@tree.command(name='avatar', description="Returns a user's avatar", guild=discord.Object(id=980162247299059792))
async def self(interaction: discord.Interaction, member: discord.Member = None):
    if member == None:
        member = interaction.user
        
    name = member.name + '#' + member.discriminator
    pfp = member.display_avatar
    color = member.color
    
    embed = discord.Embed(title='Avatar', color=color)
    embed.set_author(name=name, icon_url=pfp.url)
    embed.set_image(url=pfp.url)
    
    await interaction.response.send_message(embed=embed)
    
bot.run(TOKEN)
    
## Legacy (Prefix Commands)

# # Events
# @bot.event
# async def on_ready():
#     log.info(f"Ganyu is online as {bot.user}.")

# @bot.event
# async def on_member_join(member):
#     channel = member.guild.system_channel
#     await channel.send(f'{member.mention} Welcome To The Server!')
    
# # Commands
# @bot.command()
# async def ping(ctx):
#     await ctx.reply(f"Pong! ({bot.latency*1000:.2f}ms)")
    
# @bot.command(aliases=['8ball'])
# async def eightball(ctx, *, query):
#     responses = ["It is certain.","It is decidedly so.","Without a doubt.","Yes definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]
#     await ctx.send(f'**Question:** {query}\n**Answer:** {random.choice(responses)}')
    
# @bot.command(aliases=['avatar'])
# async def av(ctx, member: discord.Member = None):
#     if member == None:
#         member = ctx.author
        
#     name = member.name + '#' + member.discriminator
#     pfp = member.display_avatar
#     color = member.color
    
#     embed = discord.Embed(title='Avatar', color=color)
#     embed.set_author(name=name, icon_url=pfp.url)
#     embed.set_image(url=pfp.url)
    
#     await ctx.send(embed=embed)