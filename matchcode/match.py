from datetime import datetime, timedelta
import random
from numpy import random as rand

from loggingbm import logger

class Match:
    def __init__(self, home_team, away_team, year, month, day):
        self.home_team = home_team
        self.away_team = away_team
        self.year = year
        self.month = month
        self.day = day
        self.home_goals = None
        self.away_goals = None
        self.played = False
        self.is_over = False
        self.time_since_last_goal = 0
        self.events = []

    def play(self, manager_team, is_playoff):
        self.home_goals = 0
        self.away_goals = 0
        position_list = ["goalkeeper","libero","leftdef","rightdef","lefthalf","righthalf","leftmid","centralmid","rightmid","leftattack","rightattack","sub1","sub2","sub3","sub4","sub5"]
        off_weight = [2,2,3,3,8,8,12,12,12,19,19]
        def_weight = [20,16,14,14,10,10,4,4,4,2,2]
        home_team_players = self.home_team.get_players()
        away_team_players = self.away_team.get_players()

        home_off_total = 0
        away_off_total = 0
        home_def_total = 0
        away_def_total = 0
        if manager_team == self.home_team.name or manager_team == self.away_team.name:
            print(f"Manager game {manager_team}")

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

        self.home_goals = rand.poisson(3*home_off_total/away_def_total)
        self.away_goals = rand.poisson(3*away_off_total/home_def_total)
        #print (f"  -  {self.league.name} is playoff = {is_playoff}")
        if is_playoff and self.home_goals == self.away_goals:
            if rand.randint(1,100)<=60:
                self.home_goals +=1
                #print("  -  home team  won on overtime")
            else:
                self.away_goals +=1
                #print("  -  away team won on overtime")
        self.played = True

        if is_playoff:
            print(f"Is playoff: Yes")
            logger.debug(f"Playoff check {self.league.name}")
            self.league.check_elimination_quarterfinal(self.home_team, self.away_team)
            self.league.check_elimination_semifinal(self.home_team, self.away_team)
            self.league.check_elimination_final(self.home_team, self.away_team)

        #print(f"  --  in play -- {self.played}: {self.home_goals} - {self.away_goals}")

    def add_goal_event(self, team,time):
        #print(team.players)
        player_list = list(team.players.values())
        goal_scorer = random.choice(player_list)
        assist_chance = random.random()
        assisting_player = None

        if assist_chance < 0.75:
            assisting_player = random.choice(player_list)

        event = {
            "type": "goal",
            "time": time,
            "team": team.name,
            "goal_scorer": goal_scorer,
            "assisting_player": assisting_player if assisting_player else None,
            "goal_type": "Play goal"
        }

        self.events.append(event)

    def update_state(self,manager,game_time_delta):
        position_list = ["goalkeeper","libero","leftdef","rightdef","lefthalf","righthalf","leftmid","centralmid","rightmid","leftattack","rightattack","sub1","sub2","sub3","sub4","sub5"]
        off_weight = [2,2,3,3,8,8,12,12,12,19,19]
        def_weight = [20,16,14,14,10,10,4,4,4,2,2]
        home_team_players = self.home_team.get_players()
        away_team_players = self.away_team.get_players()

        time = manager.get_current_time()

        home_off_total = 0
        away_off_total = 0
        home_def_total = 0
        away_def_total = 0
        #if manager_team == self.home_team.name or manager_team == self.away_team.name:
        #    print(f"Manager game {manager_team}")

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

        self.time_since_last_goal += game_time_delta
        if (self.time_since_last_goal>10 and random.randint(1, 1000) <= 5):
            self.time_since_last_goal = 0
            home_goal_chance = random.randint(1,int(20*home_off_total/away_def_total))
            away_goal_chance = random.randint(1,int(20*away_off_total/home_def_total))
            if away_goal_chance > home_goal_chance:
                self.away_goals += 1
                self.add_goal_event(self.away_team,time)
            else:
                self.home_goals += 1
                self.add_goal_event(self.home_team,time)

    def winner(self):
        if self.played and self.home_goals is not None and self.away_goals is not None:
            if self.home_goals > self.away_goals:
                return self.home_team
            elif self.away_goals > self.home_goals:
                return self.away_team
        return None

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

    def involves_team(self, team):
        return team == self.home_team or team == self.away_team


