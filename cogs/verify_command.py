# Verify command
# verifies is target-user exist in database
# and set verification value


import discord
from discord.ext import commands
from urllib.request import urlopen
import json
from User import BotUser
import manage_users
import AOE_API_constants as constants
import script_functions as functions

# Creating verify_cmd
class verify_cmd(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    # Bot event: print a message when the bot is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print('Verify Commands ready')

    
    @commands.command()
    @commands.has_role("Moderators")    
    async def verify(self,ctx,user: discord.Member):

        user_id = user.id
        user_key= str(user_id)
        filename = constants.users_file

        is_new = manage_users.verify_new_user(filename,user_id)

        if is_new == True:

            with open(filename, 'r') as file:
                data = json.load(file)
      
            data[user_key]["verified"]="\u2705"


            with open(filename, 'w') as file:
                json.dump(data, file)
            
            await ctx.send(f'El usuario {user.name} ahora esta verificado \u2705')

        else:
            await ctx.send(f'ERROR: El usuario {user.name} no esta registrado')

    
    @commands.command()
    @commands.has_role("Moderators")    
    async def uncheck(self,ctx,user: discord.Member):

        user_id = user.id
        user_key= str(user_id)
        filename = constants.users_file

        is_new = manage_users.verify_new_user(filename,user_id)

        if is_new == True:

            with open(filename, 'r') as file:
                data = json.load(file)
      
            data[user_key]["verified"]="\u274C"


            with open(filename, 'w') as file:
                json.dump(data, file)
            
            await ctx.send(f'El usuario {user.name} ha sido invalidado \u274C')

        else:
            await ctx.send(f'ERROR: El usuario {user.name} no esta registrado')

    


        


        
      
        

async def setup(bot):
    await bot.add_cog(verify_cmd(bot))
