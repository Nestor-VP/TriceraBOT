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
def add_new_user(json_file,discord_id,aoe_id):

    # Now Open Json File and save new user
    new_user = BotUser(discord_id,aoe_id)

    with open(json_file, mode='r') as users_list:
        data = json.load(users_list)

        
    # Append(update) the new dict to the list and overwrite whole file

    with open(json_file, mode='w') as new_list:
        data.update(new_user.dictionary)
        json.dump(data, new_list)
    
    print("data updated")


# Sorts users-file list according to 1 parameter
# needs to be improved - Done 
# Last update: sort_users now accepts arguments
def sort_users(json_file,elo_type,rank_type):

    # Read the users-list Json File and parse it into a dictionary

    with open(json_file,'r') as users_list:
        data = json.load(users_list)

    sorted_users = sorted(data.keys(),key=lambda x:data[x][elo_type],reverse=True)

    #print(sorted_users)

    #sorted_dictionary = {key: data[key] for key in sorted_users}

    position = 1

    for key in sorted_users:
        
        data[key][rank_type]= position
        position += 1


    #print(data)

    with open(json_file,'w') as users_list:
        json.dump(data, users_list)




