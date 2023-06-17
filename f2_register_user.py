
# Command to register a new player by nickname and stores Data in a JSON fil
# Works!



import discord
from discord.ext import commands
from urllib.request import urlopen
import json

import os
from dotenv import load_dotenv

load_dotenv()
token1 = os.getenv('TOKEN1')

description = 'aoe2:DE bot'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix='!', description=description, intents=intents)


@client.event
async def on_ready():
    print('bot is ready!')


@client.command()
async def register(ctx, nickname):
    temp1 = {}
    temp1[nickname]=nickname
    
    # Now Open Json File and save new user

    filename = "./nicknames.json"

    with open(filename, mode='r') as f:
        lst = json.load(f)

        #print(lst)
    # Append(update) the new dict to the list and overwrite whole file

    with open(filename, mode='w') as f:
        lst.update({nickname:nickname})
        json.dump(lst, f)

    
    await ctx.send(f'el nickname {temp1} ahora esta registrado')
    

client.run(token1)