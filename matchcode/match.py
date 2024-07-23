from datetime import datetime, timedelta
import random
from numpy import random as rand

from loggingbm import logger

class Match:
    def __init__(self, home_team, away_team, year: int, month: int, day: int):
        self.home_team = home_team
        self.away_team = away_team
        self.year = year
        self.month = month
        self.day = day
        self.home_goals: int|None = None
        self.away_goals: int|None = None
        self.played: bool = False
        self.is_over: bool = False
        #self.time_since_last_goal: int = 0
        self.idle_time_left: int = 0
        self.game_state: int = 0
        '''
            0 = Standard state
            1 = Corner to home team
            2 = Corner to away team
        '''
        self.events = []

    def play(self, manager_team: str, is_playoff: bool):
        self.home_goals = 0
        self.away_goals = 0
        position_list = ["goalkeeper","libero","leftdef","rightdef","lefthalf","righthalf","leftmid","centralmid","rightmid","leftattack","rightattack","sub1","sub2","sub3","sub4","sub5"]
        off_weight: list[int] = [2,2,3,3,8,8,12,12,12,19,19]
        def_weight: list[int] = [20,16,14,14,10,10,4,4,4,2,2]
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

    def add_goal_event(self, team,time, goal_type: str):
        #print(team.players)
        player_list = list(team.players.values())
        goal_scorer = random.choice(player_list)
        assist_chance = random.random()
        assisting_player = None

        if assist_chance < 0.75:
            assisting_player = random.choice(player_list)
            if goal_scorer == assisting_player:
                assisting_player = None

        event = {
            "type": "goal",
            "time": time,
            "team": team.name,
            "goal_scorer": goal_scorer,
            "assisting_player": assisting_player if assisting_player else None,
            "goal_type": goal_type
        }

        self.events.append(event)

    def add_corner_event(self, team,time):


        event = {
            "type": "corner",
            "time": time,
            "team": team.name,
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

        if self.idle_time_left > 0:
            self.idle_time_left -= game_time_delta
            if self.idle_time_left < 0:
                self.idle_time_left = 0



        if (self.idle_time_left==0):
            event_number = random.randint(1, 1000)

            if (self.game_state == 0 and event_number<5):
                self.idle_time_left = rand.randint(6,15)
                home_goal_chance = random.randint(1,int(20*home_off_total/away_def_total))
                away_goal_chance = random.randint(1,int(20*away_off_total/home_def_total))
                if away_goal_chance > home_goal_chance:
                    self.away_goals += 1
                    self.add_goal_event(self.away_team,time, "Play goal")
                else:
                    self.home_goals += 1
                    self.add_goal_event(self.home_team,time, "Play goal")
            
            elif (self.game_state == 0 and event_number<15):
                self.idle_time_left = rand.randint(6,15)
                home_corner_chance = random.randint(1,int(20*home_off_total/away_def_total))
                away_corner_chance = random.randint(1,int(20*away_off_total/home_def_total))
                if away_corner_chance > home_corner_chance:
                    self.game_state = 2
                    self.add_corner_event(self.away_team,time)
                else:
                    self.game_state = 1
                    self.add_corner_event(self.home_team,time)

            elif (self.game_state == 1):
                self.game_state = 0
                if(event_number<300):
                    self.home_goals += 1
                    self.add_goal_event(self.home_team,time, "Corner goal")

            elif (self.game_state == 2):
                self.game_state = 0
                if(event_number<300):
                    self.away_goals += 1
                    self.add_goal_event(self.away_team,time, "Corner goal")



    def winner(self):
        if self.played and self.home_goals is not None and self.away_goals is not None:
            if self.home_goals > self.away_goals:
                return self.home_team
            elif self.away_goals > self.home_goals:
                return self.away_team
        return None

    def load_match(self, home_goals: int, away_goals: int,played: bool):
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


