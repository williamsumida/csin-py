import random
import math
from match import Match
from championship import Championship
        




def get_players():
    players = [ 

                '1',
                '2',
                '3',
                '4',
                '5',
                '6',
                '7',
                '8',
                '9',
                '10',
            ]

    random.shuffle(players)
    return players



def get_teams(players):
   ... 


players = get_players()
championship = Championship()
championship.create_wingman_teams(players)
championship.create_rounds()
