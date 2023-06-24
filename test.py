import discord
from discord.ext import commands
from urllib.request import urlopen
import json
from User import BotUser
import manage_users
import AOE_API_constants as constants
import script_functions as functions

filename= constants.users_file

with open(filename, 'r') as users_list:
    data=json.load(users_list)

print(data)

aoe_id = data['323486994040750081']["aoe_id"]

print(" ")
print(" ")

print(data['323486994040750081'])

aoe_user = BotUser(323486994040750081,aoe_id)

print(" ")
print(" ")

print(aoe_user.dictionary)

print(" ")
print(" ")

print(aoe_user.value)

#print(data)
#print(data['323486994040750081'])
#print(data['323486994040750081']['aoe_name'])
"""
my_dict={"hola":123,"fea":456,"adsad":543}

data['323486994040750081']=my_dict

print(data)"""