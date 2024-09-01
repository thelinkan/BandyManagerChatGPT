from datetime import datetime, timedelta
import random
import math
from numpy import random as rand

from matchcode.matchcalculations import calculate_distance_between_players, calculate_speed_for_tick, calculate_shortest_distance, calculate_direction

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
        self.field_width: int = 60
        self.field_length: int = 100
        #self.time_since_last_goal: int = 0
        self.idle_time_left: int = 0
        self.game_state: str = "Pre game"

        # Store player positions for both teams
        self.home_team_positions = {}
        self.away_team_positions = {}
        self.ball_position =(self.field_width // 2,self.field_length // 2,0)
        self.ball_vector = (0,0,0)
        self.ball_possession = None  # Initially, no one has the ball
        self.starting_team_home = True
        self.stroke_off = True
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

    def add_goal_event(self, team,time, goal_type: str, game):
        #print(team.players)
        position_list = ["goalkeeper","libero","leftdef","rightdef","lefthalf","righthalf","leftmid","centralmid","rightmid","leftattack","rightattack","sub1","sub2","sub3","sub4","sub5"]
        position_number = random.randint(1,10)
        position_uuid = self.home_team.actual_positions[position_list[position_number]]["player_uuid"]
        print(f"{position_number} - {position_uuid}")
        
        player_list = list(team.players.values())
        goal_scorer = game.player_manager.find_player_by_uuid(position_uuid)
        assist_chance = random.random()
        assisting_player = None

        if assist_chance < 0.75:
            exclude_list = []
            exclude_list.append(position_number)
            position_number = random.choice([i for i in range(1,10) if i not in exclude_list])
            position_uuid = self.home_team.actual_positions[position_list[position_number]]["player_uuid"]
            assisting_player = game.player_manager.find_player_by_uuid(position_uuid)
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

    def update_state(self, game, manager, game_time_delta):
        position_list = ["goalkeeper","libero","leftdef","rightdef","lefthalf","righthalf","leftmid","centralmid","rightmid","leftattack","rightattack","sub1","sub2","sub3","sub4","sub5"]
        time = manager.get_current_time()
        for i in range(11):
            #print(i)

            position_uuid = self.home_team.actual_positions[position_list[i]]["player_uuid"]
            player = self.home_team.players[position_uuid]
            self.move_player(player,"home",position_list[i], game_time_delta)
            #print(f"{time} __ {self.home_team_positions[position_list[i]]}")

            position_uuid = self.away_team.actual_positions[position_list[i]]["player_uuid"]
            player = self.away_team.players[position_uuid]
            self.move_player(player,"away",position_list[i], game_time_delta)

        self.update_ball_position(game_time_delta)

        print(f"{time}: {self.game_state} -- {self.get_player_with_possession()}/{self.ball_position}")
        if(self.game_state == "pre game"):
            self.game_state = "playing"
        if(self.game_state == "homegoal"):
            self.home_goals += 1
            self.set_ball_possession("away","leftattack")
            self.reset_positions_after_goal()
            self.game_state = "stroke off"
        if(self.game_state == "awaygoal"):
            self.home_goals += 1
            self.set_ball_possession("home","leftattack")
            self.reset_positions_after_goal()
            self.game_state = "stroke off"
        if(self.game_state == "homekeepers"):
            self.set_ball_possession("home","goalkeeper")
            self.ball_position = (self.home_team_positions['goalkeeper'][0], self.home_team_positions['goalkeeper'][1], 0)
            self.game_state = "playing"
        if(self.game_state == "awaykeepers"):
            self.set_ball_possession("away","goalkeeper")
            self.ball_position = (self.away_team_positions['goalkeeper'][0], self.away_team_positions['goalkeeper'][1], 0)
            #print(self.away_team_positions['goalkeeper'])
            self.game_state = "playing"

        #print(f"{time} __{self.ball_position} : {self.ball_vector}")
        '''
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
                    self.add_goal_event(self.away_team,time, "Play goal", game)
                else:
                    self.home_goals += 1
                    self.add_goal_event(self.home_team,time, "Play goal", game)
            
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
                    self.add_goal_event(self.home_team,time, "Corner goal", game)

            elif (self.game_state == 2):
                self.game_state = 0
                if(event_number<300):
                    self.away_goals += 1
                    self.add_goal_event(self.away_team,time, "Corner goal", game)
        '''
    def update_ball_position(self, time_delta: int) -> None:
        """
        Updates the position and vector of the ball.

        :param time_delta: The time elapsed since the last update (in seconds).
        :param player_with_ball: The player object who has possession of the ball, if any.
        """
        player_with_ball = self.get_player_with_possession()
        #print(f"Player with ball: {player_with_ball}")
        if player_with_ball[1] is not None:
            # Player has possession, ball follows player's movement.
            if(player_with_ball[0]=="home"):
                self.ball_position = (self.home_team_positions[player_with_ball[1]][0], self.home_team_positions[player_with_ball[1]][1], 0)
            else:
                self.ball_position = (self.away_team_positions[player_with_ball[1]][0], self.away_team_positions[player_with_ball[1]][1], 0)
            self.ball_vector = (0, 0, 0)
        else:
            # No possession, update ball position based on its vector.
            self.ball_position = (
                self.ball_position[0] + self.ball_vector[0] * time_delta,
                self.ball_position[1] + self.ball_vector[1] * time_delta,
                self.ball_position[2] + self.ball_vector[2] * time_delta
            )

            # If the ball is in the air (z > 0), apply gravity.
            if self.ball_position[2] > 0 or self.ball_position[2] < 0:
                friction_coefficient = 0.90
                self.ball_vector = (
                    round(self.ball_vector[0] * friction_coefficient,3),  # x component remains the same
                    round(self.ball_vector[1] * friction_coefficient,3),  # y component remains the same
                    self.ball_vector[2] - 9.81 * time_delta  # z component affected by gravity
                )
                
                # If the ball hits the ice (z <= 0), it bounces.
                if self.ball_position[2] <= 0:
                    self.ball_position = (self.ball_position[0], self.ball_position[1], -self.ball_position[1]* 0.2)
                    if(-self.ball_vector[2] * 0.1>2):
                        self.ball_vector = (
                            self.ball_vector[0] * 0.8, 
                            self.ball_vector[1] * 0.8, 
                            -self.ball_vector[2] * 0.1  # Invert and reduce z component for bounce
                        )
                    else:
                        self.ball_vector = (
                            self.ball_vector[0] * 0.8, 
                            self.ball_vector[1] * 0.8, 
                            0  # Invert and reduce z component for bounce
                        )

            
            else:
                # Ball is sliding on the ice (z = 0), apply friction to x and y components.
                friction_coefficient = 0.78  # Adjust this value as needed to simulate ice friction
                self.ball_vector = (
                    round(self.ball_vector[0] * friction_coefficient,3),
                    round(self.ball_vector[1] * friction_coefficient,3),
                    0  # No vertical movement on the ice
                )
                
                # Stop the ball if it's moving very slowly
                if abs(self.ball_vector[0]) < 0.01 and abs(self.ball_vector[1]) < 0.01:
                    self.ball_vector = (0, 0, 0)

        # Ensure ball position stays within the field boundaries
        #print(f"ball position {self.ball_position}")
        if self.ball_position[0] <= 0 or self.ball_position[0] >= self.field_width:
            # Ball hits the left or right boundary, invert the x component of the vector
            self.ball_vector = (-self.ball_vector[0], self.ball_vector[1], self.ball_vector[2])
            # Correct the ball position to stay within the boundary
            self.ball_position = (
                max(0, min(self.field_width, self.ball_position[0])),
                self.ball_position[1],
                self.ball_position[2]
            )

        if self.ball_position[1] <= 0 or self.ball_position[1] >= self.field_length:
            # Ball hits the top or bottom boundary, invert the y component of the vector
            self.ball_vector = (self.ball_vector[0], -self.ball_vector[1], self.ball_vector[2])
            # Correct the ball position to stay within the boundary
            self.ball_position = (
                self.ball_position[0],
                max(0, min(self.field_length, self.ball_position[1])),
                self.ball_position[2]
            )

        # Ensure z is not below the ice (z >= 0)
        self.ball_position = (
            self.ball_position[0],
            self.ball_position[1],
            max(0, self.ball_position[2])
        )

    def set_ball_possession(self, team: str, position: str = None) -> None:
        """Set the player in possession of the ball."""
        if team not in ["home", "away"]:
            raise ValueError("Invalid team identifier. Use 'home' or 'away'.")
        
        valid_positions = [
            "goalkeeper", "libero", "leftdef", "rightdef", 
            "lefthalf", "righthalf", "leftmid", "centralmid", 
            "rightmid", "leftattack", "rightattack", 
            "sub1", "sub2", "sub3", "sub4", "sub5"
        ]
        
        if position is not None and position not in valid_positions:
            raise ValueError("Invalid position identifier.")
        
        self.ball_possession = (team, position)

    def get_player_with_possession(self):
        """Retrieve the player object who currently has possession of the ball."""
        if self.ball_possession is None:
            return None  # No player currently has possession
        
        team, position = self.ball_possession
        
        if team == "home":
            return team, position
        elif team == "away":
            return team, position

        return None

    def move_player(self,player,home_away,player_position,game_time_delta):
        if(home_away=="home"):
            current_position = self.home_team_positions[player_position]
        else:
            current_position = self.away_team_positions[player_position]
        #print(self.home_team_positions)
        #print(current_position)
        last_vector = (current_position[2],current_position[3])

        # Step 1: Decision Logic
        decision, target_player = self.calculate_decision(player, home_away, player_position, current_position)
        if target_player is None:
            target_player_position = (-1,-1)
        else:   
            if(target_player[0]=="home"):
                target_player_position = self.home_team_positions[target_player[1]]
            else:
                target_player_position = self.away_team_positions[target_player[1]]

        speed_old = math.sqrt(last_vector[0]**2 + last_vector[1]**2)
        skating = player.get_attribute("Skating").level
        acceleration = player.get_attribute("Acceleration").level
        max_speed = skating/10
        max_acceleration = (acceleration / 100) * 4
        new_acceleration = max_acceleration/2
        speed_new = min(max_speed,speed_old+new_acceleration)

        # Determine the desired direction (e.g., towards the ball, a teammate, or an open space)
        desired_direction = self.calculate_desired_direction(player,home_away,player_position, decision, target_player_position)
        #print(desired_direction)
        # Calculate the angle between the last vector and the desired direction

        angle_between = self.calculate_angle(last_vector, desired_direction)
        # Limit the angle change based on speed
        max_turn_angle = self.calculate_max_turn_angle(last_vector)

        if angle_between > max_turn_angle:
            # Smoothly transition the direction
            new_direction = self.interpolate_direction(last_vector, desired_direction, max_turn_angle)
        else:
            new_direction = desired_direction
        #print(f"movement: {home_away}/{player_position} {current_position} - {last_vector} - {desired_direction} - {angle_between}")

        #target_position = (0,0)
        #direction_vector = (target_position[0] - current_position[0], 
        #                target_position[1] - current_position[1])
        vector_length = math.sqrt(new_direction[0]**2 + new_direction[1]**2)
        if vector_length > 0:
            direction_vector = (new_direction[0] / vector_length, new_direction[1] / vector_length)
        else:
            direction_vector = (0,0)
        move_distance = min(speed_new, vector_length)
        #if(player_position=="leftattack"):

        new_position = (current_position[0] + direction_vector[0] * move_distance,
                    current_position[1] + direction_vector[1] * move_distance, direction_vector[0] * move_distance, direction_vector[1] * move_distance) 

        if(home_away=="home"):
            self.home_team_positions[player_position] = new_position 
        else:
            self.away_team_positions[player_position] = new_position

        if(decision == "throw"):
            max_throw_vector = 8
            self.set_ball_possession(home_away,None)
            # Calculate the vector from current position to the target position
            throw_vector = (
                target_player_position[0] - current_position[0],
                target_player_position[1] - current_position[1],
                0  # z-value is 0 for throws along the ice
            )
            
            # Calculate the magnitude of the throw vector (Euclidean distance)
            vector_magnitude = math.sqrt(throw_vector[0]**2 + throw_vector[1]**2)
            
            # If the magnitude is greater than the max allowed, scale it down
            if vector_magnitude > max_throw_vector:
                scaling_factor = max_throw_vector / vector_magnitude
                self.ball_vector = (
                    throw_vector[0] * scaling_factor,
                    throw_vector[1] * scaling_factor,
                    0
                )
            else:
                self.ball_vector = throw_vector
                
        if(decision == "pass"):
            max_pass_vector = 12
            self.set_ball_possession(home_away,None)
            # Calculate the vector from current position to the target position
            pass_vector = (
                target_player_position[0] - current_position[0],
                target_player_position[1] - current_position[1],
                0  # z-value is 0 for throws along the ice
            )
            
            # Calculate the magnitude of the throw vector (Euclidean distance)
            vector_magnitude = math.sqrt(pass_vector[0]**2 + pass_vector[1]**2)
            
            # If the magnitude is greater than the max allowed, scale it down
            if vector_magnitude > max_pass_vector:
                scaling_factor = max_pass_vector / vector_magnitude
                self.ball_vector = (
                    pass_vector[0] * scaling_factor,
                    pass_vector[1] * scaling_factor,
                    0
                )
            else:
                self.ball_vector = pass_vector

        if(player_position == "goalkeeper"):
            #print(f"{player_position}: {self.away_team_positions}")
            pass
        if(decision == "shoot"):
            print("Decision = Shoot")
            self.game_state = self.action_attempt_shot(player, home_away,player_position)
        



        #print(f"{current_position} - {new_position}")            

    def calculate_desired_direction(self, player,home_away,player_position, decision, target_player_position):
        """
        Determines the desired direction for the player based on their position 
        and current game context.
        """
        #print(player)
        if player_position == 'goalkeeper':
            return self._goalkeeper_direction_logic(player,home_away,player_position, decision, target_player_position)
        elif player_position in ['libero', 'leftdef', 'rightdef']:
            return self._defender_direction_logic(player,home_away,player_position, decision, target_player_position)
        elif player_position in ['lefthalf', 'righthalf']:
            return(0,0)
        elif player_position in ['leftmid', 'centralmid', 'rightmid']:
            return(0,0)
        elif player_position in ['leftattack', 'rightattack']:
            return self._attacker_direction_logic(player,home_away,player_position, decision, target_player_position)
        else:
            #return self._general_direction_logic(player)
            return(0,0)

    def _goalkeeper_direction_logic(self,player,home_away,player_position, decision, target_player_position):
        if(home_away=="home"):
            current_position = self.home_team_positions[player_position]
        else:
            current_position = self.away_team_positions[player_position]
        if(home_away=="home"):
            target_position = (30,0)
        else:
            target_position = (30,100)

        return calculate_direction(current_position, target_position)
    
    def _defender_direction_logic(self,player,home_away,player_position, decision, target_player_position):
        if(home_away=="home"):
            current_position = self.home_team_positions[player_position]
        else:
            current_position = self.away_team_positions[player_position]

        possession = self.get_player_with_possession()
        if(possession == None):
            if(home_away=="home"):
                position_map = {
                    "leftdef": (self.field_width // 2 - 20, 20),
                    "libero": (self.field_width // 2, 16),
                    "rightdef": (self.field_width // 2 + 20, 20)
                }
            else:
                position_map = {
                    "rightdef": (self.field_width // 2 - 20, self.field_length-20),
                    "libero": (self.field_width // 2, self.field_length-16),
                    "leftdef": (self.field_width // 2 + 20, self.field_length-20)
                }
            target_position = position_map.get(player_position, (30, 50))

            return calculate_direction(current_position, target_position)
        if(possession[0]==home_away):
            if(possession[1]==player_position):
                if(home_away=="home"):
                    position_map = {
                        "leftdef": (self.field_width // 2 - 20, 20),
                        "libero": (self.field_width // 2, 16),
                        "rightdef": (self.field_width // 2 + 20, 20)
                    }
                else:
                    if(decision == "dribble"):
                        position_map = {
                            "rightdef": (self.field_width // 2 + 10, self.field_length-18),
                            "libero": (self.field_width // 2 + 30, self.field_length-16),
                            "leftdef": (self.field_width // 2 - 10 , self.field_length-18)
                        }
                    else:
                        position_map = {
                            "rightdef": (self.field_width // 2 - 20, self.field_length-20),
                            "libero": (self.field_width // 2, self.field_length-16),
                            "leftdef": (self.field_width // 2 + 20, self.field_length-20)
                        }

                target_position = position_map.get(player_position, (30, 50))

                return calculate_direction(current_position, target_position)


            else:
                if(home_away=="home"):
                    position_map = {
                        "leftdef": (self.field_width // 2 - 20, 20),
                        "libero": (self.field_width // 2, 16),
                        "rightdef": (self.field_width // 2 + 20, 20)
                    }
                else:
                    position_map = {
                        "rightdef": (self.field_width // 2 - 20, self.field_length-20),
                        "libero": (self.field_width // 2, self.field_length-16),
                        "leftdef": (self.field_width // 2 + 20, self.field_length-20)
                    }
                target_position = position_map.get(player_position, (30, 50))

                return calculate_direction(current_position, target_position)
        else:
            if(home_away=="home"):
                position_map = {
                    "leftdef": (self.field_width // 2 - 20, 20),
                    "libero": (self.field_width // 2, 16),
                    "rightdef": (self.field_width // 2 + 20, 20)
                }
            else:
                position_map = {
                    "rightdef": (self.field_width // 2 - 20, self.field_length-20),
                    "libero": (self.field_width // 2, self.field_length-16),
                    "leftdef": (self.field_width // 2 + 20, self.field_length-20)
                }
            target_position = position_map.get(player_position, (30, 50))

            return calculate_direction(current_position, target_position)

     
    def _attacker_direction_logic(self,player,home_away,player_position, decision, target_player_position):
        if(home_away=="home"):
            current_position = self.home_team_positions[player_position]
        else:
            current_position = self.away_team_positions[player_position]

        possession = self.get_player_with_possession()
        if(possession == None):
            if(home_away=="home"):
                position_map = {
                    "leftattack": (self.field_width // 2 + 20, 70),
                    "rightattack": (self.field_width // 2 - 20, 60)
                }
            else:
                position_map = {
                    "leftattack": (self.field_width // 2 - 20, self.field_length-70),
                    "rightattack": (self.field_width // 2 + 20, self.field_length-60)
                }
            target_position = position_map.get(player_position, (30, 50))

            return calculate_direction(current_position, target_position)
        if(possession[0]==home_away):
            if(possession[1]==player_position):
                if(home_away=="home"):
                    position_map = {
                        "leftattack": (self.field_width // 2 + 10, 90),
                        "rightattack": (self.field_width // 2 - 10, 90)
                    }
                else:
                    position_map = {
                        "leftattack": (self.field_width // 2 - 20, self.field_length-70),
                        "rightattack": (self.field_width // 2 + 20, self.field_length-60)
                    }
                target_position = position_map.get(player_position, (30, 50))

                return calculate_direction(current_position, target_position)

            else:
                if(home_away=="home"):
                    position_map = {
                        "leftattack": (self.field_width // 2 + 20, 70),
                        "rightattack": (self.field_width // 2 - 20, 60)
                    }
                else:
                    position_map = {
                        "leftattack": (self.field_width // 2 - 20, self.field_length-70),
                        "rightattack": (self.field_width // 2 + 20, self.field_length-60)
                    }
                target_position = position_map.get(player_position, (30, 50))

                return calculate_direction(current_position, target_position)
        else:
            if(home_away=="home"):
                position_map = {
                    "leftattack": (self.field_width // 2 + 20, 70),
                    "rightattack": (self.field_width // 2 - 20, 60)
                }
            else:
                position_map = {
                    "leftattack": (self.field_width // 2 - 20, self.field_length-70),
                    "rightattack": (self.field_width // 2 + 20, self.field_length-60)
                }
            target_position = position_map.get(player_position, (30, 50))
            return calculate_direction(current_position, target_position)

    def calculate_angle(self, vec1, vec2):
        """Calculates the angle between two vectors."""
        dot_product = vec1[0] * vec2[0] + vec1[1] * vec2[1]
        magnitude_vec1 = math.sqrt(vec1[0] ** 2 + vec1[1] ** 2)
        magnitude_vec2 = math.sqrt(vec2[0] ** 2 + vec2[1] ** 2)
        magnitude_multi = magnitude_vec1 * magnitude_vec2
        if magnitude_vec1 * magnitude_vec2 == 0:
            return 0
        if dot_product/magnitude_multi >= 1 or dot_product/magnitude_multi <= -1:
            return 0      
        return math.acos(dot_product / (magnitude_multi))

    def calculate_max_turn_angle(self, last_vector):
        """
        Determines the maximum angle by which a player can turn 
        based on their speed.
        """
        # Calculate the magnitude (speed) of the last vector
        speed = math.sqrt(last_vector[0]**2 + last_vector[1]**2)        
        # Simple example: The faster the player, the smaller the max turn angle
        # This value can be fine-tuned based on how you want players to behave.
        return max(10, 90 - speed * 2)  # Just an example

    def interpolate_direction(self, vec1, vec2, max_angle):
        """Interpolates between two directions by a limited angle."""
        angle_between = self.calculate_angle(vec1, vec2)
        ratio = min(1, max_angle / angle_between)
        return (
            vec1[0] * (1 - ratio) + vec2[0] * ratio,
            vec1[1] * (1 - ratio) + vec2[1] * ratio
        )

    def calculate_decision(self, player, home_away, player_position, current_position):
        """
        Determines the desired direction for the player based on their position 
        and current game context.
        """
        #print(player)
        if player_position == 'goalkeeper':
            return self._goalkeeper_decision_logic(player,home_away,player_position)
        elif player_position in ['libero', 'leftdef', 'rightdef']:
            return self._defender_decision_logic(player,home_away,player_position)
        elif player_position in ['lefthalf', 'righthalf']:
            return self._half_decision_logic(player,home_away,player_position)
        elif player_position in ['leftmid', 'centralmid', 'rightmid']:
            return "off-the-ball", None
        elif player_position in ['leftattack', 'rightattack']:
            return self._attacker_decision_logic(player,home_away,player_position)
        else:
            return "off-the-ball", None
        # Implement the decision logic based on player role, ball position, etc.
        # Return a decision (e.g., "shoot", "pass", "move")
        return "dribble"

    def _goalkeeper_decision_logic(self,player,home_away,player_position):
        if(home_away=="home"):
            current_position = self.home_team_positions[player_position]
        else:
            current_position = self.away_team_positions[player_position]

        goal_position = (self.field_width // 2, self.field_length) if home_away == "home" else (self.field_width // 2, 0)
        possession = self.get_player_with_possession()
        if(possession == None):
            return "off-the-ball",None
        elif(possession[0]==home_away):
            if(possession[1]==player_position):
                #print(f"{possession[1]} -- {player_position}")
                # Define the possible target positions and their probabilities
                targets = [
                    (home_away, "leftdef"),
                    (home_away, "rightdef"),
                    (home_away, "libero")
                ]
                probabilities = [0.25, 0.25, 0.50]  # Corresponding probabilities

                # Select a target based on the defined probabilities
                target = random.choices(targets, probabilities)[0]

                # Return the action and the selected target
                return "throw", target
            else:
                return "off-the-ball", None
        else:
            return "off-the-ball", None

    def _defender_decision_logic(self,player,home_away,player_position):
        if(home_away=="home"):
            current_position = self.home_team_positions[player_position]
        else:
            current_position = self.away_team_positions[player_position]

        possession = self.get_player_with_possession()
        if(possession[1] == None):
            if(self.ball_position[2]==0):
                ball_position = (self.ball_position[0],self.ball_position[1])
                ball_vector = (self.ball_vector[0],self.ball_vector[1])
                shortest_distance_to_ball = calculate_shortest_distance(ball_position, ball_vector, (current_position[0],current_position[1]))
                #print(f"{home_away}/{player_position} - {shortest_distance_to_ball}")
                if(shortest_distance_to_ball<0.3):
                    self.ball_possession=(home_away,player_position)
            return "off-the-ball",None
        elif(possession[0]==home_away):
            if(possession[1]==player_position):
                decision_list = [
                    ("dribble",None),
                    ("pass",(home_away,"lefthalf")),
                    ("pass",(home_away,"righthalf"))
                ]
                probabilities = [0.70, 0.15, 0.15]  # Corresponding probabilities

                # Select a target based on the defined probabilities
                decision = random.choices(decision_list, probabilities)[0]

                return decision
            else:
                return "off-the-ball", None
        else:
            return "off-the-ball", None

    def _half_decision_logic(self,player,home_away,player_position):
        if(home_away=="home"):
            current_position = self.home_team_positions[player_position]
        else:
            current_position = self.away_team_positions[player_position]

        possession = self.get_player_with_possession()
        if(possession[1] == None):
            if(self.ball_position[2]==0):
                ball_position = (self.ball_position[0],self.ball_position[1])
                ball_vector = (self.ball_vector[0],self.ball_vector[1])
                shortest_distance_to_ball = calculate_shortest_distance(ball_position, ball_vector, (current_position[0],current_position[1]))
                #print(f"{home_away}/{player_position} - {shortest_distance_to_ball}")
                if(shortest_distance_to_ball<0.3):
                    self.ball_possession=(home_away,player_position)
            return "off-the-ball",None

        return "off-the-ball",None

    def _attacker_decision_logic(self,player,home_away,player_position):
        if(home_away=="home"):
            current_position = self.home_team_positions[player_position]
        else:
            current_position = self.away_team_positions[player_position]

        goal_position = (self.field_width // 2, self.field_length) if home_away == "home" else (self.field_width // 2, 0)
        
        # Calculate distance to the goal
        distance_to_goal = math.sqrt((goal_position[0] - current_position[0])**2 + 
                                    (goal_position[1] - current_position[1])**2)

        possession = self.get_player_with_possession()
        if(possession == None):
            return "off-the-ball", None
        elif(possession[0]==home_away):
            if(possession[1]==player_position):
                #print(f"{possession[1]} -- {player_position}")
                if distance_to_goal < 20:  # Close enough to shoot
                    return self._shoot_or_dribble_logic(distance_to_goal), None
                else:
                    return "dribble", None
            else:
                return "off-the-ball", None
        else:
            return "off-the-ball", None

    def _shoot_or_dribble_logic(self, distance_to_goal):
        """
        Decides whether to shoot or dribble based on distance to the goal and other factors.
        """
        # Example: The closer the player, the higher the chance to shoot
        shoot_chance = max(0.2, 1 - (distance_to_goal / 20))  # Simple probability based on distance
        
        if random.random() < shoot_chance:
            return "shoot"
        else:
            return "dribble"

    def action_attempt_shot(self, player, home_away,player_position):
        shot_quality = self.calculate_shot_quality(player, home_away, player_position)
        if(shot_quality>15):
            if(home_away=="home"):
                return "homegoal"
            else:
                return "awaygoal"
        else:
            if(home_away=="home"):
                return "awaykeepers"
            else:
                return "homekeepers"
        

    def calculate_shot_quality(self, player, home_away, player_position):
        if(home_away=="home"):
            current_position = self.home_team_positions[player_position]
        else:
            current_position = self.away_team_positions[player_position]

        goal_position = (self.field_width // 2, self.field_length) if home_away == "home" else (self.field_width // 2, 0)
        
        # Calculate distance to the goal
        distance_to_goal = math.sqrt((goal_position[0] - current_position[0])**2 + 
                                    (goal_position[1] - current_position[1])**2)

        # Calculate the angle relative to the goal
        angle = math.degrees(math.atan2(abs(current_position[0] - goal_position[0]), current_position[1] - goal_position[1]))

        
        shooting = player.get_attribute("Shooting")
        shooting_level = shooting.level
        distance_factor = max(0,-0.003333*distance_to_goal**2 - 0.03333*distance_to_goal +1)

        if distance_to_goal < 3 or angle > 135:
            angle_factor = 1
        elif 90 <= angle <= 135:
            angle_factor = (angle - 90) / 45
        else:
            angle_factor = 0

        base_quality = shooting_level * distance_factor * angle_factor
        R = base_quality * 0.3 + 20
        random_factor = random.uniform(-R, R)
        final_quality = base_quality + random_factor
        final_quality = max(0, min(100, final_quality))

        print(f"shoot {distance_to_goal}:{angle} __ {shooting_level}/{round(distance_factor,5)}/{round(angle_factor,5)} ___ {final_quality}")
        return final_quality

        

    def set_initial_positions(self):
        # Set up the home team and away team positions
        self._set_team_positions(self.home_team, home_side=True)
        self._set_team_positions(self.away_team, home_side=False)

    def _set_team_positions(self, team, home_side):
        positions = {}
        center_x = self.field_width // 2
        center_y = self.field_length // 2

        if home_side:
            # Positions for the home team (all on their own half)
            positions['goalkeeper'] = (center_x, int(1),0,0)
            positions['libero'] = (center_x, int(0.08 * self.field_length),0,0)
            positions['leftdef'] = (int(0.3 * self.field_width), int(0.17 * self.field_length),0,0)
            positions['rightdef'] = (int(0.7 * self.field_width), int(0.17 * self.field_length),0,0)
            positions['lefthalf'] = (int(0.15 * self.field_width), int(0.25 * self.field_length),0,0)
            positions['righthalf'] = (int(0.85 * self.field_width), int(0.25 * self.field_length),0,0)
            positions['leftmid'] = (int(0.2 * self.field_width), int(0.37 * self.field_length),0,0)
            positions['centralmid'] = (center_x, int(0.30 * self.field_length),0,0)
            positions['rightmid'] = (int(0.8 * self.field_width), int(0.37 * self.field_length),0,0)
            if(self.starting_team_home==True):
                positions['leftattack'] = (center_x, center_y,0,0)
                positions['rightattack'] = (center_x-2, center_y-1,0,0)
            else:
                positions['leftattack'] = (int(0.35 * self.field_width), int(0.45 * self.field_length),0,0)
                positions['rightattack'] = (int(0.65 * self.field_width), int(0.45 * self.field_length),0,0)

            self.home_team_positions = positions

        else:
            # Positions for the away team (all on their own half)
            positions['goalkeeper'] = (center_x, int(self.field_length-1),0,0)
            positions['libero'] = (center_x, int(0.92 * self.field_length),0,0)
            positions['leftdef'] = (int(0.7 * self.field_width), int(0.83 * self.field_length),0,0)
            positions['rightdef'] = (int(0.3 * self.field_width), int(0.83 * self.field_length),0,0)
            positions['lefthalf'] = (int(0.85 * self.field_width), int(0.75 * self.field_length),0,0)
            positions['righthalf'] = (int(0.15 * self.field_width), int(0.75 * self.field_length),0,0)
            positions['leftmid'] = (int(0.8 * self.field_width), int(0.63 * self.field_length),0,0)
            positions['centralmid'] = (center_x, int(0.70 * self.field_length),0,0)
            positions['rightmid'] = (int(0.2 * self.field_width), int(0.63 * self.field_length),0,0)
            if(self.starting_team_home==False):
                positions['leftattack'] = (center_x, center_y,0,0)
                positions['rightattack'] = (center_x+2, center_y+1,0,0)
            else:
                positions['leftattack'] = (int(0.65 * self.field_width), int(0.55 * self.field_length),0,0)
                positions['rightattack'] = (int(0.35 * self.field_width), int(0.55 * self.field_length),0,0)

            self.away_team_positions = positions

        #print(positions)


    def reset_positions_after_goal(self):
        self.set_initial_positions()

    def reset_positions_at_halftime(self):
        self.set_initial_positions()



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


