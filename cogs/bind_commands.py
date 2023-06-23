# Commands for Binding Discord-User with Xbox/Steam Account
# Command List:
#   !bind: Binds Discord.Account with Xbox/Steam Account
#   !unbind: Deletes association among Discord.Account and desired platform-account
#   !rebind: Deletes old association and creates a new one.
# Status: Working


import discord
from discord.ext import commands
from urllib.request import urlopen
import json
from User import BotUser
import manage_users
import AOE_API_constants as constants
import script_functions as functions

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
    # platform_id: Xbox or Steam User-ID-number
    @commands.command()
    async def bind(self,ctx,platform,platform_id):

        Discord_id = ctx.message.author.id  # Get Command-author Discord ID

        #check if platform-input is correct
        platformVal = functions.eval_platform(platform)


        # User's info file path
        filename = constants.users_file

        is_new = manage_users.verify_new_user(filename,Discord_id)

        if is_new == True:
            await ctx.send(f'ERROR: el usuario <@{Discord_id}> ya existe')
            await ctx.send(f'Para ver la lista de commandos , digitar: !List')
            return
        elif platformVal== 'error':
            await ctx.send(f'ERROR: Ingrese una plataforma válida ( Xbox or Steam)')
            return
        else:
            pass

        manage_users.add_new_user(filename,Discord_id,platform,platform_id)

        await ctx.send(f'el usuario <@{Discord_id}> ahora esta registrado')
        
      
        

async def setup(bot):
    await bot.add_cog(bind_cmd(bot))
