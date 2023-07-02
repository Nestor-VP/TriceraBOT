# Command:  !info *Discord.User
# Retrieves Desired user Player Card  
# if empty retrieves command.author Player Card

import discord
from discord.ext import commands
from urllib.request import urlopen
import json
from User import BotUser
import manage_users
import AOE_API_constants as constants
import script_functions as functions
from discord import Embed


#Creating info_cmd class

class info_cmd(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    #Bot event: print a message when the bot is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print('info command ready')
    

    # !info command: Retrieves desired user Player-Card
    # The command recieves desired user Discord.name as argument
    # if empty the command retrives command-author Player-Card
    @commands.command()
    async def info(self,ctx,username: str=None):

        # if username is a discord Member or User discord object

        filename = constants.users_file

        if username is None:
            username = ctx.author.id
            
        else:
            username= username.strip("@<>")
            # username = username.id
            
        
        #Deploy some code that search in JSON if there's a Key with username-value
        user_exist = manage_users.verify_new_user(filename,username)

        if user_exist:
            user = await self.bot.fetch_user(username)

            with open(filename, 'r') as users_list:
                data=json.load(users_list)
            
            key_str = str(username)

            aoe_name = data[key_str]["aoe_name"]
            elo_single=data[key_str]["elo_single"]
            elo_team=data[key_str]["elo_team"]
            rank_single=data[key_str]["rank_single"]
            rank_team=data[key_str]["rank_team"]
            bot_role= data[key_str]["ladder_role"]
            check_status= data[key_str]["verified"]


            embed = Embed(title= None,
                          description= f"__**<@{username}> CARD: **__  {check_status}",  # Set the description of the embed
                        color=discord.Color.green()
                          )
            
            embed.add_field(name="", value=f"**AOE nickname: ** {aoe_name} ",inline=False)
            embed.add_field(name="", value=f"**ELO 1v1: ** {elo_single}",inline=False)
            embed.add_field(name="", value=f"**Rank 1v1: ** {rank_single}",inline=False)
            embed.add_field(name="", value=f"**ELO team: ** {elo_team}",inline=False)
            embed.add_field(name="", value=f"**Rank team: ** {rank_team}",inline=False)
            embed.add_field(name="", value=f"**AOE role: ** {bot_role} ",inline=False)
            # embed.set_thumbnail(url=user.avatar)  //  if user hasnt upload an avatar return None , consider using display_avatar
            embed.set_thumbnail(url=manage_users.get_avatar(bot_role))

            
            await ctx.send(embed=embed)
            
    
        else:
            await ctx.send("El usuario no esta registrado")



async def setup(bot):
    await bot.add_cog(info_cmd(bot))