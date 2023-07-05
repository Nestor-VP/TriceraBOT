# update-roles Cog
# Update-Task: On all users - Updates aoe-Roles according to their 1v1 ELO


import discord
from discord.ext import commands, tasks
from urllib.request import urlopen
import json
from User import BotUser
import manage_users
import AOE_API_constants as constants
import script_functions as functions
import elos_update

#Creating update_cmd class

class update_roles_task(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.roles_update.start()
    
    
    def cog_unload(self):
        self.roles_update.cancel()
    
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('update-roles task ready')

    
    @tasks.loop(hours=12.0)
    async def roles_update(self):

        guild_id = 1117856688964390952
        guild = await self.bot.fetch_guild(guild_id)
        channel = self.bot.get_channel(1123673745748406333) # Anuncios Channel

        filename = constants.users_file
        elos_update.update_all_elos(filename)

        with open(filename, 'r') as users_list:
                data=json.load(users_list)
        
        for key in data:
            key_int = int(key)
            elo = data[key]["elo_single"]
            old_role = data[key]["ladder_role"]
            new_role = manage_users.calc_role(elo)
            member = await guild.fetch_member(key_int)

            if old_role=="Developer":
                 new_role="Developer"

            old_role_name = manage_users.get_role_name(old_role)
            new_role_name = manage_users.get_role_name(new_role)
            discord_old_role = discord.utils.get(guild.roles, name=old_role_name)
            #discord_dev_role= discord.utils.get(guild.roles, name="Developers")
            discord_new_role = discord.utils.get(guild.roles, name=new_role_name)

            if old_role != new_role:
                    await member.add_roles(discord_new_role)
                    await member.remove_roles(discord_old_role)

        
        arg_time = functions.get_current_hour(-3)
        # get Peru time
        peru_time = functions.get_current_hour(-5)
        await channel.send(f"```Roles Updated \nLast update: Perú ( {peru_time} ) | Argentina ( {arg_time} ) ```")   


    @roles_update.before_loop
    async def before_update(self):
        print('updating roles...')
        await self.bot.wait_until_ready()               


async def setup(bot):
    await bot.add_cog(update_roles_task(bot)) 