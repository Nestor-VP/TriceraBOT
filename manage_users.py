# manage_users.py   
# Script that contains some required functions to manage the Bot-users
# function list:
# verify_new_user
# add_new_user
# Sort_user
# calc_role
# get_role_name
# get_avatar
# update_server_stats   - new function v2 - update all user's ELOs and Ratings


import json
from User import BotUser
import AOE_API_constants as constants
import discord
from discord.ext import commands
from discord import Embed
import Avatars


# verify_new_user -> verifies if a discord.id is already registered
# True if user exist in database
# False if user doesnt exist in databasa - New User
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
    
    #print("data updated")


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



# Calc User-AOE-role based on his elo_single
def calc_role(elo):

    intervals = [(800 + i * 200, 800 + (i + 1) * 200) for i in range(5)]
    values = ['Aldeano', 'Milicia', 'Hombre de Armas', 'Espadachín', 'Espada Mandoble', 'Campeón', 'Legionario']
    
    for i in range(len(intervals)):
        interval = intervals[i]
        value = values[i+1]
        
        if elo >= interval[0] and elo < interval[1]:
            return value
    
    if elo < 800:
        return values[0]
    elif elo >= 1800:
        return values[6]
    

# Get_role_name : Returns the role-name(Exactly how they are named in the discord-guild)

def get_role_name(role):
    cases = {
        'Aldeano': 'Aldeanos',
        'Milicia': 'Milicias',
        'Hombre de Armas': 'Hombres de armas',
        'Espadachín': 'Espadachines',
        'Espada Mandoble': 'Espadas Mandobles',
        'Campeón': 'Campeones',
        'Legionario': 'Legionarios',
    }

    return cases.get(role, 'Aldeanos')


def get_avatar(role):
    cases = {
        'Aldeano': Avatars.AV1,
        'Milicia': Avatars.AV2,
        'Hombre de Armas': Avatars.AV3,
        'Espadachín': Avatars.AV4,
        'Espada Mandoble': Avatars.AV5,
        'Campeón': Avatars.AV6,
        'Legionario': Avatars.AV7,
        'Developer': Avatars.AV_DEV
    }

    return cases.get(role, 'Aldeanos')



#
# Command to change unicode-emoji into ascii-character
# just for printing purposes
def emoji_2ascii(value):

    
    if value=="\u2705":
        return "■"
    else:
        return "x"
    

# Update_server_stats automatically
# command to update ELOS and Ratins from all registered users
# Recieves as parameter user's list file location

def update_server_stats(json_file):

    with open(json_file,'r') as data:
        users_list = json.load(data)
    
    for key in users_list:
        aoe_id = users_list[key]["aoe_id"]
        ladder_role= users_list[key]["ladder_role"]
        verified = users_list[key]["verified"]

        aoe_user= BotUser(key,aoe_id)

        aoe_user.verified = verified
        aoe_user.role = ladder_role

        users_list[key]=aoe_user.value
    
    with open(json_file, mode='w') as new_list:
                json.dump(users_list, new_list)

    sort_users(json_file,"elo_single","rank_single")
    sort_users(json_file,"elo_team","rank_team") 











   



