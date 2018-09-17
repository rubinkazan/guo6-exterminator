# Work with Python 3.6
import discord
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()
guo6_id = 135680632402608128
TOKEN = 'NDkwODM1MDk0ODA2ODU1NzAy.Dn_Rug.6QqSZvAym3MQw-ZrgnDbh8i8nKI'

async def guo6_exterminator(context):
    response = 'diam dog'
    await client.say(response) + context.message.author.mention

description = '''Responds with diam dog everytime guo6 sends a message'''

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if client.user.id:
        msg = 'Diam Dog {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Bot Loaded')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(TOKEN)
#https://discordapp.com/oauth2/authorize?&client_id=490835094806855702&scope=bot&permissions=238173312
