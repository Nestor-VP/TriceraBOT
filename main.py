import discord
import os
import asyncio
from discord.ext import commands
import BOT_functions as botfx

# Retrieve token key
token = botfx.get_token()

# Creating a Bot object
bot = commands.Bot(command_prefix='!',intents=discord.Intents.all(),case_insensitive=True)


# Bot event: print  a message when the bot is ready ( online)
@bot.event
async def on_ready():
    print(f'Logged is as {bot.user}')

# Bot command: Command to load a file extension (specific Cog File)
@bot.command()
async def load(ctx,extension):
    await bot.load_extension(f'cogs.{extension}')

# Bot command: Command to unload a file extension ( specific Cog file)
@bot.command()
async def unload(ctx,extension):
    await bot.unload_extension(f'cogs.{extension}')

# Script function that loads all file extension from Cog folder
async def load_files():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')

# Script main function 
async def main():
    await load_files()
    await bot.start(token)

# run main function
asyncio.run(main())