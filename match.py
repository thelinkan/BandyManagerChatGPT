from datetime import datetime, timedelta
import random

class Match:
    def __init__(self, home_team, away_team, year, month, day):
        self.home_team = home_team
        self.away_team = away_team
        self.year = year
        self.month = month
        self.day = day
        self.home_goals = 0
        self.away_goals = 0
        self.played = False

    def play(self):
        position_list = ["goalkeeper","libero","leftdef","rightdef","lefthalf","righthalf","leftmid","centralmid","rightmid","leftattack","rightattack","sub1","sub2","sub3","sub4","sub5"]
        off_weight = [2,2,3,3,8,8,12,12,12,19,19]
        def_weight = [20,16,14,14,10,10,4,4,4,2,2]
        home_team_players = self.home_team.get_players()
        away_team_players = self.away_team.get_players()
        
        home_off_total = 0
        away_off_total = 0
        home_def_total = 0
        away_def_total = 0
        
        for i in range(11):
            #print(i)
            
            position_uuid = self.home_team.actual_positions[position_list[i]]["player_uuid"]
            player = self.home_team.players[position_uuid]
            composite_values = player.calculate_composite_values(position_list[i])
            home_off_total += composite_values[0] * off_weight[i]
            home_def_total += composite_values[1] * def_weight[i]

            position_uuid = self.away_team.actual_positions[position_list[i]]["player_uuid"]
            player = self.away_team.players[position_uuid]
            composite_values = player.calculate_composite_values(position_list[i])
            away_off_total += composite_values[0] * off_weight[i]
            away_def_total += composite_values[1] * def_weight[i]

        #print(f"{self.home_team.name} ({home_off_total},{home_def_total}) - {self.away_team.name} ({away_off_total},{away_def_total})")
        #print(f"{player.first_name} {player.last_name} -  {player.calculate_composite_values(position_list[0])}")
        
        self.home_goals = random.randint(0, 10)
        self.away_goals = random.randint(0, 10)
        self.played = True

    def load_match(self, home_goals, away_goals,played):
        self.home_goals = home_goals
        self.away_goals = away_goals
        self.played = played
        #print (f"{self.home_team.name} - {self.away_team.name}    {self.home_goals}-{self.away_goals}")

    def to_dict(self):
        #print (f"{self.home_team.name} - {self.away_team.name}    {self.home_goals}-{self.away_goals}")
        return {
            'home_team': self.home_team.name,
            'away_team': self.away_team.name,
            'year': self.year,
            'month': self.month,
            'day': self.day,
            'home_goals': self.home_goals,
            'away_goals': self.away_goals,
            'played': self.played
        }


