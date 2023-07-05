#Unbind command - ADMIN COMMAND
#Unbinds target-user with Associated AOE-ID
# Deletes all target-users info
# target-user will lost all his AOE-roles

import discord
from discord.ext import commands
from urllib.request import urlopen
import json
from User import BotUser
import manage_users
import AOE_API_constants as constants
import script_functions as functions

class unbind_cmd(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    # Bot event: print a message when the bot is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print('Unbind command ready')
    

    # !UnBind command: Admin command to deleted target-user associations
    # username: discord-user ( in mention format @name)
    @commands.command()
    @commands.has_role("Developers")
    async def unbind(self,ctx,user: discord.Member):

        user_id = user.id
        user_key = str(user_id)

        aoe_roles = ["Aldeanos","Milicias","Hombres de armas","Espadachines","Espadas Mandobles","Campeones","Legionarios"]
      
       
        # User's info file path
        filename = constants.users_file

        is_new = manage_users.verify_new_user(filename,user_id)

        if is_new == True:

            for role in aoe_roles:

                aoe_role = discord.utils.get(ctx.guild.roles, name=role)
                if aoe_role in user.roles:
                    await user.remove_roles(aoe_role)
        
            await ctx.send(f'Los roles-AOE de {user.mention} fueron borrados')    

            with open(filename, 'r') as file:
                data = json.load(file)


            key_to_delete = user_key
            
            if key_to_delete in data:
                del data[key_to_delete]


            with open(filename, 'w') as file:
                json.dump(data, file)

            functions.subtract_one_user()
            await ctx.send(f"El Usuario {user.mention} ha perdido el registro.")
                
            
        else:
            await ctx.send(f'ERROR: El usuario no esta registrado.')
            return
            

               
        
        
      
        

async def setup(bot):
    await bot.add_cog(unbind_cmd(bot))