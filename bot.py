# bot.py
import os
import random
import pprint as pp
import discord
from discord.ext import commands
from dotenv import load_dotenv
from championship import Championship
from team import Team

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
COMMAND_CREATE_WINGMAN_TEAMS='create wingman teams'

bot = commands.Bot(command_prefix='!')


@bot.command(name='ajuda')
async def help(ctx):
    msg  = "9? 99? 999?\n"
    msg += "Comando: !patifaria\n"
    msg += "Descricao: sorteia 2 times e move os jogadores para as salas Time 1 e Time 2\n"
    msg += "Obs1: todos os jogadores devem estar em uma mesma sala (nao importa qual sala)\n"
    msg += "Obs2: o comando pode ser usado pra criar partidas NxN, se N for impar, NxN+1\n\n"
    
    msg += "Comando: !wingman player1, player2, ..., playerN\n"
    msg += "Descricao: sorteia a lista de jogadores e os separa em N/2 times"

    await ctx.send(msg)


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
   

@bot.command(name='patifaria')
async def create_5v5(ctx):
    members_in_current_channel = []
    team_1 = []
    team_2 = []
    author = ctx.author
    
    voice_channels = ctx.guild.voice_channels
    voice_channel_1, voice_channel_2 = get_5v5_channels(voice_channels)

    for channel in voice_channels:
        if author in channel.members:
            members_in_current_channel = channel.members
    
    team_1, team_2 = sort_5v5_teams(members_in_current_channel)
    if team_1:
        for player in team_1:
            await player.move_to(voice_channel_1)
    if team_2:
        for player in team_2:
            await player.move_to(voice_channel_2)


@bot.command(name='despatifaria')
async def move_players_from_teams_to_main_channel(ctx):
    voice_channels = ctx.guild.voice_channels
    
    lobby_channel = get_lobby_channel(voice_channels)
    voice_channel_1, voice_channel_2 = get_5v5_channels(voice_channels)
    
    for member in voice_channel_1.members:
        await member.move_to(lobby_channel)

    for member in voice_channel_2.members:
        await member.move_to(lobby_channel)


def get_lobby_channel(voice_channels):
    channel_name='Lobby'  
    for channel in voice_channels:
        if channel.name == channel_name:
            return channel
    return channel[0]


def get_5v5_channels(voice_channels):
    voice_channel_1 = None
    voice_channel_2 = None
    for channel in voice_channels:
        if channel.name == "Time 1":
            voice_channel_1 = channel
        
        if channel.name == "Time 2":
            voice_channel_2 = channel

    return voice_channel_1, voice_channel_2


def sort_5v5_teams(members):
    random.shuffle(members)
    team_1_count = int(len(members)/2)
    team_1 = members[:len(members)//2]
    team_2 = members[len(members)//2:]
    return team_1, team_2


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
