import json
import discord
from discord.ext import commands, tasks
from table2ascii import table2ascii as t2a, PresetStyle
import AOE_API_constants as constants


class leaderboard_cmd(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Leaderboard commands ready')

    @commands.command()
    @commands.has_role("Developers")
    async def top(self,ctx,elo_key: str=None):

        filename= constants.users_file

        if elo_key is None:
            await ctx.send("For 1v1 Leaderboard, type: !Top S")
            await ctx.send("For Team Leaderboard, type: !Top T")
        elif elo_key in ['s', 'S']:

            with open(filename,'r') as users_list:
                data = json.load(users_list)

            sorted_users = sorted(data.keys(),key=lambda x:data[x]["elo_single"],reverse=True)
            
            position = 1
            table = []

            for key in sorted_users:

                elo_single=data[key]["elo_single"]

                # GOT SOME PROBLEMS RETRIEVING discord-guild-nickname  --> WILL TRY TO FIX IT in a future
                #int_key= int(key)
               # username = await ctx.guild.get_member(int_key)
               # nickname=username.nick
                aoe_name = data[key]["aoe_name"]
                table.append([position,elo_single,aoe_name])
                position += 1

            header=["Rank", "ELO", "nick-AOE"]
            output = t2a(header,table,style=PresetStyle.thin_compact)

            
            await ctx.send(f"```\nLeaderboard- Random Map 1v1\n{output}\n```")


        elif elo_key in ['t', 'T']:
            
            
            with open(filename,'r') as users_list:
                data = json.load(users_list)

            sorted_users = sorted(data.keys(),key=lambda x:data[x]["elo_team"],reverse=True)
            
            position = 1
            table = []

            for key in sorted_users:

                elo_team=data[key]["elo_team"]

                # GOT SOME PROBLEMS RETRIEVING discord-guild-nickname  --> WILL TRY TO FIX IT in a future
                #int_key= int(key)
                #username = await ctx.guild.get_member(int_key)
                #nickname=username.nick
                aoe_name = data[key]["aoe_name"]
                table.append([position,elo_team,aoe_name])
                position += 1

            header=["Rank", "ELO", "nick-AOE"]
            output = t2a(header,table,style=PresetStyle.thin_compact)

            
            await ctx.send(f"```\nLeaderboard- Random Map Team\n{output}\n```")
        else:
            await ctx.send("For 1v1 Leaderboard, type: !Top S")
            await ctx.send("For Team Leaderboard, type: !Top T")

async def setup(bot):
    await bot.add_cog(leaderboard_cmd(bot))  


