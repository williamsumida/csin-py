import random


class Team:
    def __init__(self):
        self.name = ''
        self.players = []

    def set_player(self, player):
        self.players.append(player)


class Championship:
    def __init__(self):
        self.name = ''
        self.type = '' # brackets or groups
        self.teams = []
        self.finals = []
        self.semifinals = []
        self.quarterfinals = []
        self.rounds = []


    def create_wingman_teams(self, players):
        while players:
            team_player_count = 2
            number_of_teams = 1
            team = Team()
            team.name = f'Time {number_of_teams}'
            for i in range(2):
                team.set_player(players.pop())
            number_of_teams += 1
            

    def random_wingman_map(self, number_of_maps):
        maps = [
                'Inferno',
                'Cobblestone',
                'Vertigo',
                'Overpass',
                'Train',
                'Rialto',
                'Lake',
                'Shortdust'
                ]
        random.shuffle(maps)
        return maps[:number_of_maps]


class Match:
   def __init__(self):
       self.teams = []
       self.winner = []
       self.score = '' 



def get_players():
    players = [ 
                'eltao',
                'will',
                'igawa',
                'jimmy',
                'chorao',
                'robin',
                'feeder',
                'aron',
                'toico',
                'xaxo'
            ]

    random.shuffle(players)
    return players



def get_teams(players):
   ... 


players = get_players()
championship = Championship()
championship.create_wingman_teams(players)