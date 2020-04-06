import random

class Match:
    def __init__(self):
        self.teams = []
        self.winner = ''
        self.loser = ''
        self.map_pool = []
        self.score = ''


    def random_wingman_map(self, number_of_maps):
        maps = ['Inferno', 
                'Cobblestone',
                'Vertigo',
                'Overpass',
                'Train',
                'Rialto',
                'Lake',
                'Shortdust'
                ]
        random.shuffle(maps)
        self.map_pool = maps[:number_of_maps]