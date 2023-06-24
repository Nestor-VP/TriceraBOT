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

        user_exist= manage_users.verify_new_user(filename,Discord_id)




async def setup(bot):
    await bot.add_cog(update_cmd(bot))   
