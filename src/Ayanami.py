import json
from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
TOKEN = json.loads(open('config.json', 'r').read())['token']

import discord
from discord.ext import commands
bot: commands.Bot = commands.Bot(command_prefix="g.", intents=discord.Intents.all())

from logger import log

import random

# Events
@bot.event
async def on_ready():
    log.info(f"Ganyu is online as {bot.user}.")

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    await channel.send(f'{member.mention} Welcome To The Server!')
    
# Commands
@bot.command()
async def ping(ctx):
    await ctx.reply(f"Pong! ({bot.latency*1000:.2f}ms)")
    
@bot.command(aliases=['8ball'])
async def eightball(ctx, *, query):
    responses = ["It is certain.","It is decidedly so.","Without a doubt.","Yes definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]
    await ctx.send(f'**Question:** {query}\n**Answer:** {random.choice(responses)}')
    
@bot.command(aliases=['avatar'])
async def av(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
        
    name = member.name + '#' + member.discriminator
    pfp = member.display_avatar
    color = member.color
    
    embed = discord.Embed(title='Avatar', color=color)
    embed.set_author(name=name, icon_url=pfp.url)
    embed.set_image(url=pfp.url)
    
    await ctx.send(embed=embed)

bot.run(TOKEN)