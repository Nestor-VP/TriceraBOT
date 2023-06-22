# test script
# create a Bind command using BotUser Class

import discord
from discord.ext import commands
from urllib.request import urlopen
import json
from User import BotUser

class bind_test(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    
    # Bot event: print a message when the bot is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bind_test commands ready')
    
    @commands.command()
    async def test(self,ctx,platform,platform_id):

        discord_id=ctx.message.author.id

        new_user = BotUser(discord_id,platform,platform_id)

        await ctx.send(f"{new_user.key_id}")
        await ctx.send(f"{new_user.platform}")
        await ctx.send(f"{new_user.aoe_name}")
        await ctx.send(f"{new_user.elo_single}")
        await ctx.send(f"{new_user.elo_team}")



async def setup(bot):
    await bot.add_cog(bind_test(bot))

