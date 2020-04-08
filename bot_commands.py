# bot.py
import os
from discord.ext import commands
import random
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
COMMAND_CREATE_WINGMAN_TEAMS='create wingman teams'


bot = commands.Bot(command_prefix='!')


@bot.command(name='create5v5')
async def create_5v5(ctx):
    #print(ctx)
    print('oi')


bot.run(TOKEN)
