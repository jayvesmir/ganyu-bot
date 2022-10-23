from logger import log
from commands import processCommands

import json
import discord

cofigContent = open('config.json', 'r').read()
TOKEN = json.loads(cofigContent)['token']
TEST_SERVER = discord.Object(id=json.loads(cofigContent)['commands_guild'])
IS_DEBUG: bool = True if str(json.loads(cofigContent).get('is_debug', 'false')).capitalize() == 'True' else False
PREFIX: str = json.loads(cofigContent)['prefix']

from discord.ext import commands
from discord import Member, Client, app_commands
bot: commands.Bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

import random

class Ganyu(Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False
              
    async def on_ready(self):
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game('with your data'))
        await tree.sync(guild=TEST_SERVER if IS_DEBUG else None)
        self.synced = True
        log().info(f'Ganyu is online as {bot.user}.')
        if IS_DEBUG:
            log('Debug').warning(f"The bot is set to debug, it's commands will only register in {TEST_SERVER.id=}")

bot = Ganyu()
tree = app_commands.CommandTree(bot)

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel:
        await channel.send(f'{member.mention} Welcome To The Server!')
    
@bot.event
async def on_message(ctx):
    if not ctx.author.bot:
        processCommands(msg=ctx.content)

@tree.command(name='ping', description='Check if the bot lives.', guild=TEST_SERVER if IS_DEBUG else None)
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong! ({bot.latency*1000:.2f}ms)')
    
@tree.command(name='eightball', description='Rolls the 8ball.', guild=TEST_SERVER if IS_DEBUG else None)
async def self(interaction: discord.Interaction, query: str):
    responses = ['It is certain.',"It is decidedly so.","Without a doubt.","Yes definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]
    await interaction.response.send_message(f'**Question:** {query}\n**Answer:** {random.choice(responses)}')
    
@tree.command(name='avatar', description="Returns a user's avatar", guild=TEST_SERVER if IS_DEBUG else None)
async def self(interaction: discord.Interaction, member: Member = None):
    if member is None:
        member = interaction.user
        
    name = member.name + '#' + member.discriminator
    pfp = member.display_avatar
    color = member.color
    
    embed = discord.Embed(title='Avatar', color=color)
    embed.set_author(name=name, icon_url=pfp.url)
    embed.set_image(url=pfp.url)
    
    await interaction.response.send_message(embed=embed)
    
bot.run(TOKEN)
