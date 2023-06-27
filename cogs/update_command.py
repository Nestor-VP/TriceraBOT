# Update command
# Retrieves Bot.message.author updated ELO-data ( retrieved from AOE2 API)
# Calls sort fuction to update Server-Users-Ranking

import discord
from discord.ext import commands
from urllib.request import urlopen
import json
from User import BotUser
import manage_users
import AOE_API_constants as constants
import script_functions as functions

#Creating update_cmd class

class update_cmd(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Update command ready')
    

    # !Update command
    @commands.command()
    async def update(self,ctx):
        Discord_id = ctx.message.author.id  # Get Command-author Discord ID

        filename= constants.users_file
        user_key = str(Discord_id)

        user_exist= manage_users.verify_new_user(filename,Discord_id)

        if user_exist:

            with open(filename, 'r') as users_list:
                data=json.load(users_list)

            
            aoe_id = data[user_key]["aoe_id"]
            old_role = data[user_key]["ladder_role"]

            role_name= manage_users.get_role_name(old_role)
            discord_old_role = discord.utils.get(ctx.guild.roles, name=role_name)
            discord_dev_role= discord.utils.get(ctx.guild.roles, name="Developers")

            # Update user data
            aoe_user = BotUser(Discord_id,aoe_id)

            if old_role=="Developer":

                aoe_user.role = "Developer"
                

            elif discord_dev_role in ctx.author.roles:

                aoe_user.role = "Developer"
                

            else:

                # Retrieve updated-elo-1v1
                new_elo = aoe_user.elo_single

                # Calc new role
                new_role= manage_users.calc_role(new_elo)

                # Save new-role in user-card
                aoe_user.role = new_role

                # Returns the role-name(Exactly how they are named in the discord-guild)
                # Playerd card role and Discord-role names are a little different because of plurals
                role_name = manage_users.get_role_name(new_role)

                discord_new_role = discord.utils.get(ctx.guild.roles, name=role_name)            

                if old_role != new_role:
                    await ctx.author.add_roles(discord_new_role)
                    await ctx.author.remove_roles(discord_old_role)
                    await ctx.send(f"{ctx.author.mention} ahora pertenece a los '{discord_new_role.name}'")



            
            
            data[user_key] = aoe_user.value

            with open(filename, mode='w') as new_list:
                json.dump(data, new_list)


            manage_users.sort_users(filename,"elo_single","rank_single")
            manage_users.sort_users(filename,"elo_team","rank_team")

            await ctx.send(f"<@{Discord_id}> data updated - please type: !info")

            

            
        

        else:
            await ctx.send("ERROR: El usuario no esta registrado")




async def setup(bot):
    await bot.add_cog(update_cmd(bot))   
