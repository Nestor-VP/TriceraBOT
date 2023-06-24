# manage_users.py   
# Script that contains some required functions to manage the Bot-users
# function list:
# verify_new_user
# add_new_user
# modify_user
# delete_user
# Sort_user
# update_leaderboard


import json
from User import BotUser
import AOE_API_constants as constants
import discord
from discord.ext import commands
from discord import Embed


# verify_new_user -> verifies if a discord.id is already registered
def verify_new_user(json_file,key):
    with open(json_file, 'r') as users_list:
        data=json.load(users_list)
    #convert Key-number into a string
    key_str = str(key)

    return key_str in data
    
# Adds a new-user-dictionary to the Users-list Json File
def add_new_user(json_file,discord_id,platform,platform_id):

    # Now Open Json File and save new user
    new_user = BotUser(discord_id,platform,platform_id)

    with open(json_file, mode='r') as users_list:
        data = json.load(users_list)

        
    # Append(update) the new dict to the list and overwrite whole file

    with open(json_file, mode='w') as new_list:
        data.update(new_user.dictionary)
        json.dump(data, new_list)
    
    print("data updated")


# Sorts users-file list according to 1 parameter
# needs to be improved
def sort_users(json_file):

    # Read the Json File and parse it into a dictionary

    with open(json_file,'r') as users_list:
        data = json.load(users_list)

    sorted_users = sorted(data.keys(),key=lambda x:data[x]["elo_team"],reverse=True)

    print(sorted_users)

    #sorted_dictionary = {key: data[key] for key in sorted_users}

    position = 1

    for key in sorted_users:
        
        data[key]["ladder_rank"]= position
        position += 1


    print(data)


# This function retrieves Discord.User-Dictionary
# and creates a discord.Embed to show its game-info

async def player_card(json_file,key,user):

    key_str=str(key)

    with open(json_file,'r') as users_list:
        data = json.load(users_list)
    
    user_info=data[key_str]

    embed = Embed(
            title=f'Player info',  # Set the title of the embed
            description= f'<@{key}> stats:',  # Set the description of the embed
            color=discord.Color.blue()  # Set the color of the embed
        )

        # Add fields to the embed
    embed.add_field(name=user_info["elo_team"], value='Value 1', inline=False)  # Add a field with a name and value (not inline)
    embed.add_field(name='Field 2', value='Value 2', inline=True)  # Add a field with a name and value (inline)

        # Set an image for the embed
    
    avatar_url = user.avatar_url
    

    embed.set_thumbnail(url=avatar_url)  # Set the image URL for the embed
    embed.set_image(url='https://i.imgur.com/UoKS5Tr.png')
        # Send the embed message to the channel
    # await ctx.send(embed=embed)
    # We Shall return embed
    





filename = constants.users_file

sort_users(filename)









''' Test Commands

filename = "./nicknames.json"

add_new_user(filename,2313,"STEAM", 76561198260505584)

'''