# bot.py
import os
import discord
import random
from dotenv import load_dotenv
from championship import Championship
from team import Team

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
COMMAND_CREATE_WINGMAN_TEAMS='create wingman teams'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if COMMAND_CREATE_WINGMAN_TEAMS in message.content.lower():
        players = get_players(message.content)
        if(len(players) % 2 != 0):
            await message.channel.send('Número ímpar de jogadores, alguem se fudeu')
            players.pop()

        championship = Championship()
        teams = championship.create_wingman_teams(players)
        final_message=format_teams_message(teams)

        await message.channel.send(final_message)


def format_teams_message(teams):
    final_message = '\n'
    for team in teams:
        final_message += f'{team.name}: {team.players[0]} e {team.players[1]}\n'
    return final_message


def get_players(message: str):
    players_string = message.replace(COMMAND_CREATE_WINGMAN_TEAMS, '')
    players_list = list(players_string.split(','))
    random.shuffle(players_list)
    print(players_list)
    return players_list


client.run(TOKEN)
