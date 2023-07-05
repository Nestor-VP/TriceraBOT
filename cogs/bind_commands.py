# Commands for Binding Discord-User with an AOE-account
# Command List:
#   !bind: Binds Discord.Account with AOE Account


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
    

    # !Bind command: Command to Bind Discord.Account with AOE Account
    # aoe_id: AOE User-ID-number
    @commands.command()
    async def bind(self,ctx,aoe_id):

        Discord_id = ctx.message.author.id  # Get Command-author Discord ID
        user_key = str(Discord_id)

        # User's info file path
        filename = constants.users_file

        is_new = manage_users.verify_new_user(filename,Discord_id)

        if is_new == True:
            await ctx.send(f'ERROR: el usuario <@{Discord_id}> ya existe')
            #await ctx.send(f'Para ver la lista de commandos , digitar: !List')
            return
        
        else:
            #  code = Verify ID function
            # if code == False:
            #   await ctx.send(f'ERROR: Ingrese un aoe_Id valido')
            #   await ctx.send(f'Para mayor informacion revise <#Bot-tutorial>')
            #   return
            # Else: pass
            pass

        manage_users.add_new_user(filename,Discord_id,aoe_id)
        manage_users.sort_users(filename,"elo_single","rank_single")
        manage_users.sort_users(filename,"elo_team","rank_team")

        with open(filename, 'r') as users_list:
                data=json.load(users_list)
        
        new_role = data[user_key]["ladder_role"]
        role_name= manage_users.get_role_name(new_role)
        discord_new_role = discord.utils.get(ctx.guild.roles, name=role_name)
        

        await ctx.send(f'el usuario <@{Discord_id}> ahora esta registrado')
        await ctx.author.add_roles(discord_new_role) 
        await ctx.send(f"{ctx.author.mention} ahora pertenece a los {discord_new_role.name}") # Cambiar a rol calculado
        
      
        

async def setup(bot):
    await bot.add_cog(bind_cmd(bot))
