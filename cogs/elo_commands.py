import discord
from discord.ext import commands
from urllib.request import urlopen
import json

# Creating elo_cmd class
# This class will have methods to retrive the AOE2 ELO
class elo_cmd(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    # Bot event: print a message when the bot is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print('ELO commands ready')

    # Bot command: Command to Retrieve user ELOs
    @commands.command()
    async def elo(self,ctx,nickname):
        
        # Abrir URL.
        r = urlopen(f"https://aoe2.net/api/leaderboard?game=aoe2de&leaderboard_id=4&start=1&count=1&search={nickname}")

        dictionary1 = r.read()
        print(dictionary1)
    
        my_dict = json.loads(dictionary1.decode('utf-8'))
        sub_dict = my_dict['leaderboard']
        dict2= sub_dict[0]
        elo = dict2['rating']
        print(elo)
        await ctx.send(f'{elo}')


async def setup(bot):
    await bot.add_cog(elo_cmd(bot))