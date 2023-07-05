# Auto Update Cog
# Update-Task: On all users - Updates Elos and Sort them according to new-elos
# Command-Timer: sets Update-task period.

import discord
from discord.ext import commands, tasks
from urllib.request import urlopen
import json
from User import BotUser
import manage_users
import AOE_API_constants as constants
import script_functions as functions

#Creating update_cmd class

class update_task(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
       # self.auto_update.start()
    
    """
    def cog_unload(self):
        self.auto_update.cancel() """
    
    
    

    @commands.Cog.listener()
    async def on_ready(self):
        print('Auto-update task ready')

    """
    @tasks.loop(minutes=30.0)
    async def auto_update(self):

        filename = constants.users_file

        manage_users.update_server_stats(filename)
        pass
    """

          





async def setup(bot):
    await bot.add_cog(update_task(bot))  