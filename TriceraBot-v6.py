# Command that returns requested  User's ELO
# Generates a risponse on a discord embed
# Works!



import discord
from discord.ext import commands
from urllib.request import urlopen
from discord import Embed
import json

description = 'TriceraBOT v5'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix='!', description=description, intents=intents)


@client.event
async def on_ready():
    print('bot is ready!')

@client.command()
async def ELO(ctx,nickname):
    
    # Abrir URL.
    r = urlopen(f"https://aoe2.net/api/leaderboard?game=aoe2de&leaderboard_id=4&start=1&count=1&search={nickname}")
    # Leer el contenido y e imprimir su tamaño.
    dictionary1 = r.read()

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

    # Create an Embed object
    embed = Embed(
            title=f'Player info',  # Set the title of the embed
            description= f'<@{(ctx.message.author.id)}> stats:',  # Set the description of the embed
            color=discord.Color.blue()  # Set the color of the embed
        )

        # Add fields to the embed
    embed.add_field(name=elo, value='Value 1', inline=False)  # Add a field with a name and value (not inline)
    embed.add_field(name='Field 2', value='Value 2', inline=True)  # Add a field with a name and value (inline)

        # Set an image for the embed
    embed.set_thumbnail(url=ctx.message.author.avatar)  # Set the image URL for the embed
    embed.set_image(url='https://i.imgur.com/UoKS5Tr.png')
        # Send the embed message to the channel
    await ctx.send(embed=embed)
    
 



client.run('MTExNzg3Njk0NTc1ODE5NTg2Mg.GkdMlc.xvJwpI65ZtTl1sUDWdW46VoDLftTUI7_6dLqsI')