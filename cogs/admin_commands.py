#Admin Commands :
#useful commands to manage the server:
# users : Retrieves the number of registered users

import discord
from discord.ext import commands
from urllib.request import urlopen
import json
from User import BotUser
import manage_users
import AOE_API_constants as constants
import script_functions as functions

class admin_cmd(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    # Bot event: print a message when the bot is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print('Admin commands ready')
    

    # !users: Retrieves number of registered users
    # 
    @commands.command()
    @commands.has_role("Admins")
    async def users(self,ctx):

        users_number = functions.number_of_users()
        await ctx.send(f"Registered members: {users_number}")
    
      
        

async def setup(bot):
    await bot.add_cog(admin_cmd(bot))