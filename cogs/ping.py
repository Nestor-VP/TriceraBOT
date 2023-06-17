import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Ping Cog Loaded.')

    @commands.command()
    async def ping(self,ctx):
        await ctx.channel.send('Pong!')


async def setup(bot):
    await bot.add_cog(Ping(bot))
        

