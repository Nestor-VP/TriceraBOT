# Command that returns requested  User's ELO
# works !

import discord
from discord.ext import commands
from urllib.request import urlopen
import json
import os
from dotenv import load_dotenv

load_dotenv()
token1 = os.getenv('TOKEN1')



description = 'AOE2 BOT'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True


client = commands.Bot(command_prefix='!',intents=intents, case_insensitive=True)


@client.event
async def on_ready():
    print('bot is ready!')

@client.command()
async def ELO(ctx,nickname):
    
    # Abrir URL.
    r = urlopen(f"https://aoe2.net/api/leaderboard?game=aoe2de&leaderboard_id=4&start=1&count=1&search={nickname}")
    # Leer el contenido y e imprimir su tamaño.
    dictionary1 = r.read()
    print(dictionary1)

    # print dictionary
    # print(dictionary1)

    my_dict = json.loads(dictionary1.decode('utf-8'))
    #print(my_dict) # 👉️ {'first': 'bobby', 'last': 'hadz'}
    #print(type(my_dict)) # 👉️ <class 'dict'>
    sub_dict = my_dict['leaderboard']

    # print element from dictionary1
    #print(sub_dict)
    #print(type(sub_dict))

    # sub_dict is a dictionary inside a list , we need to retrieve the dictionary
    dict2= sub_dict[0]
    print(dict2)
    #print(type(dict2))

    elo = dict2['rating']
    print(elo)
    await ctx.send(f'{elo}')

client.run(token1)