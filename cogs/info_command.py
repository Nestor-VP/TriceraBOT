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

        filename = constants.users_file

        if username is None:
            username = ctx.author.id
        else:
            username= username.strip("@<>")
        
        #Deploy some code that search in JSON if there's a Key with username-value
        user_exist = manage_users.verify_new_user(filename,username)

        if user_exist:
            await ctx.send(f"Hello <@{username}>")

            user = await self.bot.fetch_user(username)

            embed = Embed(title='Player avatar',
                          description= f'<@{username}> stats:',  # Set the description of the embed
                        color=discord.Color.blue()
                          )
            embed.set_thumbnail(url=user.avatar.url)
            embed.set_image(url='https://i.imgur.com/UoKS5Tr.png')

            print(user)
            await ctx.send(user)
            await ctx.send(embed=embed)
            
    
        else:
            await ctx.send("El usuario no esta registrado")



async def setup(bot):
    await bot.add_cog(info_cmd(bot))