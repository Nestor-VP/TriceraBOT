import discord
import os
import asyncio
from discord.ext import commands
import BOT_functions as botfx

token = botfx.get_token()


bot = commands.Bot(command_prefix='!',intents=discord.Intents.all(),case_insensitive=True)

@bot.event
async def on_ready():
    print(f'Logged is as {bot.user}')

@bot.command()
async def cload(ctx,extension):
    await bot.load_extension(f'cogs.{extension}')

@bot.command()
async def cunload(ctx,extension):
    await bot.unload_extension(f'cogs.{extension}')

async def load():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')

async def main():
    await load()
    await bot.start(token)

asyncio.run(main())