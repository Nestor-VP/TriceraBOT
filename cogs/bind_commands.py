# Commands for Binding Discord-User with Xbox/Steam Account
# Command List:
#   !bind: Binds Discord.Account with Xbox/Steam Account
#   !unbind: Deletes association among Discord.Account and desired platform-account
#   !rebind: Deletes old association and creates a new one.


import discord
from discord.ext import commands
from urllib.request import urlopen
import json

# Creating bind_cmd class
class bind_cmd(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    # Bot event: print a message when the bot is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bind commands ready')
    

    # !Bind command: Command to Bind Discord.Account with Xbox/Steam ID
    # platform: Xbox or Steam
    # user_ID: Xbox or Steam User-ID-number
    @commands.command()
    async def bind(self,ctx,platform,user_ID):

        Discord_id = ctx.message.author.id  # Get Command-author Discord ID
       
        # Now Open Json File and save new user
        filename = "./nicknames.json"

        with open(filename, mode='r') as f:
            lst = json.load(f)        
            
        # Append(update) the new dict to the list and overwrite whole file
        with open(filename, mode='w') as f:
            lst.update({Discord_id:[platform,user_ID]})
            json.dump(lst, f)

    
        await ctx.send(f'el usuario <@{Discord_id}> ahora esta registrado')
        
      
        

async def setup(bot):
    await bot.add_cog(bind_cmd(bot))
