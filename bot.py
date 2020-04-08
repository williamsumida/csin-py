# bot.py
import os
import random
from discord.ext import commands
from dotenv import load_dotenv
from championship import Championship
from team import Team

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
COMMAND_CREATE_WINGMAN_TEAMS='create wingman teams'

bot = commands.Bot(command_prefix='!')

@bot.command(name='wingman')
async def create_wingman_teams(ctx, *, arg):
    players = get_players(arg)
    if(len(players) % 2 != 0):
        await ctx.send('Número ímpar de jogadores, alguem se fudeu')
        players.pop()

    championship = Championship()
    teams = championship.create_wingman_teams(players)
    final_message=format_teams_message(teams)
    print(final_message)
    await ctx.send(final_message)
   

@bot.command(name='5v5')
async def create_5v5(ctx):
   ... 


def format_teams_message(teams):
    final_message = '9? 99? 999?\n'
    for team in teams:
        final_message += f'{team.name}: {team.players[0]} e {team.players[1]}\n'
    return final_message


def get_players(players_string):
    players_list = list(players_string.split(','))
    random.shuffle(players_list)
    return players_list

bot.run(TOKEN)
