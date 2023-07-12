import json
import discord
from discord.ext import commands, tasks
from table2ascii import table2ascii as t2a, PresetStyle, Alignment
import AOE_API_constants as constants
import manage_users
import script_functions
import elos_update

class leaderboard_cmd(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.interval_minutes = 10
        self.rank_printer.start()
    
    def cog_unload(self):
        self.rank_printer.cancel()
    
    

    @commands.Cog.listener()
    async def on_ready(self):
        print('Leaderboard commands ready')


    @tasks.loop(minutes=30)
    async def rank_printer(self):
        
        # First task: Clear History in Hall-of-Fame Channel
        channel = self.bot.get_channel(1122349454918430772) #hall-of-fame ID: 1122349454918430772
        guild = await self.bot.fetch_guild(1117856688964390952)
        

        if channel is not None:
                async for message in channel.history(limit=None):
                    await message.delete()

        # Second task: Print Elo-Ratings-1v1

        filename= constants.users_file

        elos_update.update_all_elos(filename)
        manage_users.sort_users(filename,"elo_single","rank_single")
        manage_users.sort_users(filename,"elo_team","rank_team")

        with open(filename,'r') as users_list:
                data = json.load(users_list)

        sorted_users = sorted(data.keys(),key=lambda x:data[x]["elo_single"],reverse=True)
            
        position = 1
        table = []

        for key in sorted_users:

            elo_single=data[key]["elo_single"]
            status =  manage_users.emoji_2ascii(data[key]["verified"])
   
            int_key= int(key)
            username = await guild.fetch_member(int_key)
            nickname=username.display_name
            
            aoe_name = data[key]["aoe_name"]
            table.append([position,elo_single,nickname,aoe_name,status])
            position += 1
            if position == 11:
                 break


        header=["Rank", "ELO","nick-discord","nick-AOE","Iv"]      
        output = t2a(header,table,style=PresetStyle.thin_box)
        await channel.send(f"```\nLeaderboard Random Map - 1v1\n{output}\n```")
        
        
        # Third Task: Print ELo-Ratings-Team

        with open(filename,'r') as users_list:
                data = json.load(users_list)

        sorted_users = sorted(data.keys(),key=lambda x:data[x]["elo_team"],reverse=True)
            
        position = 1
        table = []

        for key in sorted_users:

                elo_team=data[key]["elo_team"]
                status = manage_users.emoji_2ascii(data[key]["verified"])

                int_key= int(key)
                username = await guild.fetch_member(int_key)
                nickname=username.display_name

                aoe_name = data[key]["aoe_name"]
                table.append([position,elo_team,nickname,aoe_name,status])
                position += 1
                if position == 11:
                    break

        header=["Rank", "ELO","nick-discord", "nick-AOE","Iv"]
        output = t2a(header,table,style=PresetStyle.thin_box)            
        await channel.send(f"```\nLeaderboard Random Map - Team\n{output}\n```")
        await channel.send(f"```Iv: Identity verify | verified user = ■  | non verified = x```")
        # get Argentina's time
        arg_time = script_functions.get_current_hour(-3)
        # get Peru time
        peru_time = script_functions.get_current_hour(-5)
        await channel.send(f"```Last update: Perú ( {peru_time} ) | Argentina ( {arg_time} ) ```")



        
    
    @rank_printer.before_loop
    async def before_printer(self):
        print('waiting...')
        await self.bot.wait_until_ready()
    
    
    @commands.command()
    @commands.has_role("Admins")
    async def set_interval(self, ctx, minutes: int):
        if minutes <= 0:
            await ctx.send("Please provide a positive interval.")
            return

        self.interval_minutes = minutes
        self.rank_printer.change_interval(minutes=self.interval_minutes)
        await ctx.send(f"Interval set to {self.interval_minutes} minutes.")
    



    @commands.command()
    @commands.has_role("Admins")
    async def top(self,ctx,elo_key: str=None):

        filename= constants.users_file

        if elo_key is None:
            await ctx.send("For 1v1 Leaderboard, type: !Top S")
            await ctx.send("For Team Leaderboard, type: !Top T")
        elif elo_key in ['s', 'S']:

            elos_update.update_all_elos(filename)
            manage_users.sort_users(filename,"elo_single","rank_single")
            manage_users.sort_users(filename,"elo_team","rank_team")

            with open(filename,'r') as users_list:
                data = json.load(users_list)

            sorted_users = sorted(data.keys(),key=lambda x:data[x]["elo_single"],reverse=True)
            
            position = 1
            table = []

            for key in sorted_users:

                elo_single=data[key]["elo_single"]
                status = manage_users.emoji_2ascii(data[key]["verified"])

                int_key= int(key)
                username = await ctx.guild.fetch_member(int_key)
                nickname=username.display_name
                aoe_name = data[key]["aoe_name"]
                table.append([position,elo_single,nickname,aoe_name,status])
                position += 1 
                if position == 11:
                    break        
            
            header=["Rank", "ELO","nick-discord","nick-AOE","Iv"]
            output = t2a(header,table,style=PresetStyle.thin_box)
            await ctx.send(f"```\nLeaderboard Random Map - 1v1\n{output}\n```")
            


        elif elo_key in ['t', 'T']:
            
            elos_update.update_all_elos(filename)
            manage_users.sort_users(filename,"elo_single","rank_single")
            manage_users.sort_users(filename,"elo_team","rank_team")

            with open(filename,'r') as users_list:
                data = json.load(users_list)

            sorted_users = sorted(data.keys(),key=lambda x:data[x]["elo_team"],reverse=True)
            
            position = 1
            table = []

            for key in sorted_users:

                elo_team=data[key]["elo_team"]
                status = manage_users.emoji_2ascii(data[key]["verified"])

                int_key= int(key)
                username = await ctx.guild.fetch_member(int_key)
                nickname=username.display_name
                aoe_name = data[key]["aoe_name"]
                table.append([position,elo_team,nickname,aoe_name,status])
                position += 1
                if position == 11:
                    break

            header=["Rank", "ELO","nick-discord","nick-AOE","Iv"]
            output = t2a(header,table,style=PresetStyle.thin_box)            
            await ctx.send(f"```\nLeaderboard Random Map - Team\n{output}\n```")

        else:
            await ctx.send("For 1v1 Leaderboard, type: !Top S")
            await ctx.send("For Team Leaderboard, type: !Top T")

async def setup(bot):
    await bot.add_cog(leaderboard_cmd(bot))  


