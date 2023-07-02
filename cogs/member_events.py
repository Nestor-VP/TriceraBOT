# Member_Events
# Runs tasks when a user joins/leaves the server
# On_member_Join -> Sets Villager Role , sends welcome message and instructions
# On_member_remove -> auto-deletes roles and deletes member from users-database



import discord
from discord.ext import commands
from urllib.request import urlopen
import json
from User import BotUser
import manage_users
import AOE_API_constants as constants
import script_functions as functions

# Creating member_events class
class member_events(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    # Bot event: print a message when the bot is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print('Member events ready')
    

    @commands.Cog.listener()
    async def on_member_join(self,member):
        print(f'{member} ha entrado al servidor')

        # Remember to replace with Channel Ids
        channel = self.bot.get_channel(1124963780292509707)
        new_member_role = discord.utils.get(member.guild.roles, name="Aldeanos") 
        await member.add_roles(new_member_role)
        await channel.send(f'Bienvenido {member.mention} , ahora perteneces a los {new_member_role.name}')
        await channel.send(f'Recuerda revisar la seccion <#{1124177975118680118}>') # Leer importante
        await channel.send(f'Para saber más de Teuton-BoT , revisar: <#{1124177975118680118}>') #Bot tutorial
    

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        
        print(f'{member} ha salido del servidor')
        channel = self.bot.get_channel(1124963780292509707)  # Replace with the actual ID of the channel
        

        filename = constants.users_file

        is_new = manage_users.verify_new_user(filename,member.id)
        user_key = str(member.id)

        if is_new == True:
            with open(filename, 'r') as file:
                data = json.load(file)


            key_to_delete = user_key
            
            if key_to_delete in data:
                del data[key_to_delete]


            with open(filename, 'w') as file:
                json.dump(data, file)
                
            
        else:
            await channel.send(f'ERROR: EL usuario no esta en la database')
        
        await channel.send(f"User {member} with ID {member.id} has left the guild.")
        await channel.send(f"Los Datos de {member} han sido borrados")
            
    

        
      
        

async def setup(bot):
    await bot.add_cog(member_events(bot))
