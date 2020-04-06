import math
from team import Team
from round import Round
from match import Match

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
        number_of_teams = 1
        team_player_count = 2
        while players:
            team = Team()
            team.name = f'Time {number_of_teams}'

            for i in range(team_player_count):
                team.set_player(players.pop())
            self.teams.append(team)
            number_of_teams = number_of_teams + 1

    
    def get_bound_values(self, teams_count):
        power_of_2_numbers = [2, 4, 8, 16, 32, 64]
        for n in power_of_2_numbers:
            if teams_count >= n:
                lower_value = n
            else:
                upper_value = n
                return lower_value, upper_value


    def create_matches(self, teams, is_second_round=False):
        matches = []
        if is_second_round:
            teams_per_match = 1
        else:
            teams_per_match = 2
        while teams:
            match = Match()
            match.random_wingman_map(1)
            for i in range(teams_per_match):
                match.teams.append(teams.pop())

            matches.append(match)
        return matches


    def create_rounds(self):
        teams_count = len(self.teams)
        lower_value, upper_value = self.get_bound_values(teams_count)
        
        if teams_count == lower_value:
            first_round = Round(1)
            first_round.matches = self.create_matches(self.teams)
            self.rounds.append(first_round)

        else:
            first_round = Round(1)
            second_round = Round(2)

            first_round_teams_count = upper_value - lower_value
            second_round_teams_count = teams_count - first_round_teams_count

            first_round_teams = self.teams[:first_round_teams_count]
            first_round.matches = self.create_matches(first_round_teams)


            print("first round!")
            for m in first_round.matches:
                print(m.teams[0].players, 'vs', m.teams[1].players)
                print(m.map_pool)

            second_round_teams = self.teams[-second_round_teams_count:]
            second_round.matches = self.create_matches(second_round_teams, True)

            print("second round!")
            for m in second_round.matches:
                print(m.teams[0].players, 'vs', 'TBD')
                print(m.map_pool)
    
    def is_power_of_2(self):
        n = len(self.teams)
        return math.log2(n).is_integer()
