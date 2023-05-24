import json
import random
import os
from manager import Manager
from country import Country
from club import Club
from team import Team
from league import League
from playoff import Playoff
from person import Player
from person import PlayerManager
from uuidencoder import UUIDEncoder
from matchcode.matchmanager import MatchManager

from screens.screensMatch import draw_view_match

from debug_functions import print_yesterdays_results, debugprint_playoff

class Game:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
        self.manager = Manager()
        self.countries = {}
        self.leagues = []
        self.playoffs = []
        self.clubs = []
        self.player_manager = PlayerManager()
        self.teams = {} # Add a dictionary to store teams
        self.match_manager = MatchManager()
        self.selected_player_index = -1
        self.selected_team_index = -1
        self.selected_league_index = -1
        self.selected_country_index = -1
        self.inspected_team = None
        self.inspected_league = None

        self.game_page=None

    def new_game(self,manager_name,manager_age):
        # create new game
        # Set name and age
        self.manager.set_name(manager_name)
        self.manager.set_age(manager_age)
        player_origins_male = {}
        player_origins_female = {}
        with open('data/countries.json', encoding='utf-8') as f:
            countries_data = json.load(f)
        for country_data in countries_data:
            name = country_data['name']
            bandy_knowledge = country_data['bandy_knowledge']
            population = country_data['population']
            flag_path = country_data['flag_path']
            male_proficiency = country_data['male_proficiency']
            female_proficiency = country_data['female_proficiency']
            self.countries[name] = Country(name, flag_path, bandy_knowledge, population, male_proficiency, female_proficiency)
            if 'player_origins_male' in country_data:
                player_origins_male[name] = country_data['player_origins_male']
            if 'player_origins_female' in country_data:
                player_origins_female[name] = country_data['player_origins_female']
        with open('data/clubs.json', encoding='utf-8') as f:
            data = json.load(f)
        self.clubs = self.read_clubs_from_json(data)
        for club in self.clubs:
            club_rating = club.rating
            for team in club.teams:
                team_rating = team.rating
                if (team.team_type == "Men" or team.team_type == "Men U19"):
                    gender="male"
                else:
                    gender="female"
                if (team.team_type == "Men U19" or team.team_type == "Women U19"):
                    age_type="youth"
                else:
                    age_type="senior"
                player_first_name = ""
                player_familyname = ""
                num_players_national = team.num_players
                num_players_international = team.num_int_players
                print(f"- {team.name} ({team.team_type})")
                for key, value in self.countries.items():
                    if(key == club.country):
                        team_country = value
                        team_country_name = key

                for i in range(num_players_national+num_players_international):
                    #for key, value in self.countries.items():
                    #    if(key == club.country):
                    if i < num_players_national:
                        if(gender == "male"):
                            player_first_name = team_country.random_name("male")
                        else:
                            player_first_name = team_country.random_name("female")
                        player_last_name = team_country.random_name("family")
                        nationality = team_country_name
                    else:
                        if(gender == "male"):
                            player_origins_team = player_origins_male[team_country_name]
                            player_origin = random.choices(player_origins_team, weights=[d["percentage"] for d in player_origins_team])[0]["country"]
                        else:
                            player_origins_team = player_origins_female[team_country_name]
                            player_origin = random.choices(player_origins_team, weights=[d["percentage"] for d in player_origins_team])[0]["country"]
                        for key, value in self.countries.items():
                            if(key == player_origin):
                                player_country = value
                                player_country_name = key
                                if(gender == "male"):
                                    player_first_name = player_country.random_name("male")
                                else:
                                    player_first_name = player_country.random_name("female")
                                player_last_name = player_country.random_name("family")
                                nationality = player_country_name
                    if(age_type == "youth"):
                        age = random.randint(18,19)
                    else:
                        age = random.randint(20,36)
                    if (i == 0 or i == 14):
                        position = "goalkeeper"
                    elif (i>=1 and i<=4):
                        position = "defender"
                    elif (i>=5 and i<=7):
                        position = "half back"
                    elif ((i>=8 and i<=11) or (i>=15 and i<=16)):
                        position = "midfielder"
                    elif ((i>=12 and i<=13) or (i>=17 and i<=18)):
                        position = "forward"
                    player = self.player_manager.create_player(player_first_name, player_last_name, age, gender, nationality, position, team.name)
                    player.generate_attributes(100,100,club_rating,team_rating)
                    team.add_player(player)
                    team.change_player_jersey_number(player.uuid,i+1)
                team.assign_players_to_positions()
                #team.print_players();
        with open("data/leagues.json", encoding='utf-8') as f:
            league_data = json.load(f)
        with open("data/playoffs.json", encoding='utf-8') as f:
            playoff_data = json.load(f)
        for data in league_data:
            team_names = data.pop("teams")
            #print("league data")
            #print(data)

            league_teams = []
            for team_name in team_names:
                #print(self.teams)
                team = self.teams.get(team_name, None)
                if not team:
                    raise ValueError(f"No team found with name '{team_name}'")
                league_teams.append(team)
            league = League(data["name"],data["country"],data["team_type"],data["level"],data["league_type"],league_teams,data["num_rounds"], start_month=data["startmonth"], start_day=data["startday"], end_month=data["endmonth"], end_day=data["endday"], match_manager=self.match_manager)
            if data["league_type"] == "Normal":
                league.generate_schedule()
            playoff_name = data.pop("playoff_name", None)
            if playoff_name:
                playoff = None
                for p_data in playoff_data:
                    if p_data["name"] == playoff_name:
                        playoff = Playoff(p_data["name"], p_data["country"], p_data["quarter_final_rounds"], p_data["semi_final_rounds"], p_data["final_rounds"],league, match_manager=self.match_manager)
                        self.playoffs.append(playoff)
                        print(data)
                        print(league.num_teams_to_playoff)
                        print(data["num_teams_to_playoff"])
                        league.num_teams_to_playoff=data["num_teams_to_playoff"]
                        #print(self.playoffs)
                        break
                if playoff is None:
                    raise ValueError(f"No playoff found with name '{playoff_name}'")
            self.leagues.append(league)
            #league.print_table()
            #matches = league.get_matches_by_team(team)
            #for match in matches:
            #    print(f"{match.year}-{match.month}-{match.day}")

    def load_game(self, file_path):
        # load game from file
        with open('savedgames/save_game.json', 'r', encoding='utf-8') as file:
            game_data = json.load(file)
        self.year = game_data['year']
        self.month = game_data['month']
        self.day = game_data['day']
        manager_data = game_data['manager']
        self.manager.set_name(manager_data['name'])
        self.manager.set_age(manager_data['age'])
        self.manager.set_team(manager_data['team'])
        self.countries = {}
        for country_data in game_data['countries']:
            name = country_data['name']
            bandy_knowledge = country_data['bandy_knowledge']
            population = country_data['population']
            flag_path = country_data['flag_path']
            male_proficiency = country_data['male_proficiency']
            female_proficiency = country_data['female_proficiency']
            self.countries[name] = Country(name, flag_path, bandy_knowledge, population, male_proficiency, female_proficiency)
        #print(game_data['club_data'])
        players_data = game_data.get('players_data', [])
        for player_load in players_data:
            self.player_manager.load_player(player_load["first_name"],player_load["last_name"],player_load["age"],player_load["gender"],player_load["nationality"],player_load["position"],player_load["team"],player_load["uuid"])
            player = self.player_manager.find_player_by_uuid(player_load["uuid"])
            attributes = player_load["attributes"]
            for attribute_name, attribute_data in attributes.items():
                player.set_attribute(attribute_name, attribute_data["level"], attribute_data["experience"])
                #print(attributes)

        self.clubs = self.read_clubs_from_json(game_data['club_data'])
        for club in self.clubs:
            print(club.name)
            for team in club.teams:
                print(f"- {team.name} ({team.team_type})")

        playoff_data =game_data['playoffs_data']

        for league_data in game_data['leagues_data']:
            #print(league_data['name'])
            team_names = league_data.pop("teams")
            league_teams = []
            for team_name in team_names:
                #print()
                #print(self.teams)
                #print(f"team name {team_name}")
                team = self.teams.get(team_name, None)
                if not team:
                    raise ValueError(f"No team found with name '{team_name}'")
                league_teams.append(team)
            #print(league_data)
            league = League(league_data['name'],league_data['country'],league_data["team_type"],league_data['level'],league_data['league_type'],league_teams,league_data['num_rounds'], match_manager=self.match_manager)
            league_matches = league_data['matches']
            league.load_schedule(league_matches,self.teams)
            league.calculate_table()
            playoff_name = league_data.pop("playoff_name", None)
            if playoff_name:
                playoff = None
                for p_data in playoff_data:
                    if p_data["name"] == playoff_name:
                        playoff = Playoff(p_data["name"], p_data["country"], p_data["quarter_final_rounds"], p_data["semi_final_rounds"], p_data["final_rounds"],league, match_manager=self.match_manager)
                        self.playoffs.append(playoff)
                        if "teams" in p_data:
                            team_names = p_data.pop("teams")
                            playoff_teams = []
                            for team_name in team_names:
                                #print(self.teams)
                                team = self.teams.get(team_name, None)
                                if not team:
                                    raise ValueError(f"No team found with name '{team_name}'")
                                playoff_teams.append(team)
                            playoff.teams = playoff_teams
                        playoff.is_started = p_data["is_started"]
                        #print(league_data)
                        #print(league.num_teams_to_playoff)
                        #print(league_data["num_teams_to_playoff"])
                        league.num_teams_to_playoff=league_data["num_teams_to_playoff"]
                        if "rounds" in p_data:
                            playoff.load_rounds(self,p_data["rounds"])
                        debugprint_playoff(playoff)

                        break
                if playoff is None:
                    raise ValueError(f"No playoff found with name '{playoff_name}'")

            #print(league_matches)
            self.leagues.append(league)
        #for key, value in self.countries.items():
        #    print(value.to_dict())
        print("Data loaded")
        #print(self.playoffs)
        #print(self.year)
        #print(self.manager.return_team())

    def save_game(self, file_path):
        # save game to file
        countries_data = []
        clubs_data =[]
        players = []
        players_data = []
        leagues_data = []
        playoffs_data = []

        for key, value in self.countries.items():
            countries_data.append(value.to_dict())
        for club in self.clubs:
            clubs_data.append(club.to_dict())
            for team in club.teams:
                #print(f"save: {team.name}");
                for player in team.players:
                    if player not in players:
                         players.append(player)

        for player_uuid in players:
            player = self.player_manager.find_player_by_uuid(player_uuid)
            if player is not None:
                players_data.append(player.to_dict())


        for league in self.leagues:
            leagues_data.append(league.to_dict())

        for playoff in self.playoffs:
            playoffs_data.append(playoff.to_dict())

        game_data = {
                'year': self.year,
                'month': self.month,
                'day': self.day,
                'manager': {
                    'name': self.manager.return_name(),
                    'age': self.manager.return_age(),
                    'team': self.manager.return_team()
                },
                'countries': countries_data,
                'club_data':{
                    'clubs': clubs_data
                },
                'players_data': players_data,
                'leagues_data': leagues_data,
                'playoffs_data': playoffs_data
            }
        if not os.path.exists('savedgames'):
            os.makedirs('savedgames')
        with open('savedgames/save_game.json','w', encoding='utf-8') as file:
            json.dump(game_data, file, indent=4, cls=UUIDEncoder)
        print("Game Data Saved")

    def set_manager_team(self,team):
        self.manager.set_team(team)

    def return_manager_team(self):
        self.manager.return_team

    def return_managername(self):
        return self.manager.return_name()

    def return_countrylist(self):
        countries_list = list(self.countries.values())
        countries_list.sort(key=lambda country: country.name)
        return countries_list

    def return_countries_with_leagues(self):
        countries_with_leagues = []
        for league in self.leagues:
            country = self.countries[league.country]
            if country not in countries_with_leagues:
                countries_with_leagues.append(country)
        return countries_with_leagues

    def return_countryflag(self,country_name):
         for country in self.countries.values():
            if country.name == country_name:
                return country.return_flag()

    def return_league_by_name(self, league_name):
        #print(self.leagues)
        for league in self.leagues:
            #print(f"league: {league} {league.name}")
            if league.name == league_name:
                return league
        return None

    def return_leagues_in_country(self, country_name):
        """
        Returns a list of all leagues in the specified country.
        """
        return [league for league in self.leagues if league.country == country_name]

    def return_teamlist(self, country, teamtype):
        team_list = []
        for club in self.clubs:
            if club.country == country:
                teams = club.get_teams_by_type(teamtype)
                team_list.extend(teams)
        return team_list

    def return_teams_for_league(self, league_name):
        """
        Returns a list of all teams that participate in the specified league.
        """
        teams = []
        for league in self.leagues:
            if league.name == league_name:
                teams = league.teams
                break
        return teams

    def get_leagues_for_team(self, team_name):
        """
        Returns a list of all leagues in which the specified team participates.
        """
        leagues = []
        for league in self.leagues:
            if any(team.name == team_name for team in league.teams):
                leagues.append(league)
        return leagues


    def get_leagues(self):
        return self.leagues

    def get_leagues_by_type(self, league_type):
        return [league for league in self.leagues if league.league_type == league_type]

    def read_clubs_from_json(self,data):

        clubs = []

        for club_data in data['clubs']:
            name = club_data['name']
            country = club_data['country']
            rating = club_data['club_rating']
            if 'logo' in club_data:
                logo = club_data['logo']
            else:
                logo = None
            home_arena = club_data['home_arena']
            club = Club(name, country, rating, home_arena, logo)

            for team_data in club_data['teams']:
                name = team_data['name']
                team_type = team_data['team_type']
                team_rating = team_data['team_rating']
                num_players = team_data['num_players']
                num_int_players = team_data['num_int_players']
                jersey_colors = team_data['jersey_colors']
                if 'jersey_decorations' in team_data:
                    jersey_decorations = team_data['jersey_decorations']
                else:
                    jersey_decorations = "[[0,(0,0,0)]]"
                team = Team(name, team_type, team_rating, num_players, num_int_players, jersey_colors, jersey_decorations, club)
                club.add_team(team)
                self.teams[name] = team # Add team to the dictionary
                # Check if there are players in the team_data dictionary
                if 'players' in team_data:
                    for team_player in team_data['players']:
                        player_uuid = team_player['uuid']
                        jersey_number = team_player['jersey_number']
                        # Get the Player object with the corresponding UUID
                        player = self.player_manager.find_player_by_uuid(player_uuid)
                        # Add the Player object to the team's squad
                        team.add_player(player)
                        team.change_player_jersey_number(player.uuid,jersey_number)
                if 'actual_positions' in team_data:
                    for actual_position in team_data['actual_positions']:
                        team.assign_player_to_position(actual_position['actual_position'],actual_position['player_uuid'])

            clubs.append(club)

        return clubs

    def tick(self):
        matches_today = self.match_manager.get_matches_by_date(self.year, self.month, self.day)
        match_viewed = False
        match_to_view = None
        if len(matches_today) > 0:
            for match in matches_today:
                is_playoff = False
                if self.manager.team == match.home_team.name or self.manager.team == match.away_team.name:
                    match_viewed = True
                    match_to_view = match

                    if not match.played:
                        draw_view_match(self,match_to_view)
                    if match.league.is_playoff:
                        match.league.check_elimination_quarterfinal(match.home_team, match.away_team)
                        match.league.check_elimination_semifinal(match.home_team, match.away_team)

                else:
                    print(f"    tick play {match.home_team.name} - {match.away_team.name}: {match.league.name}")
                    #if self.playoff_for_league is not None:
                    #    playoff_teams = self.playoff_for_league.teams
                    #    if match.home_team in playoff_teams and match.away_team in playoff_teams:
                    #    else:
                    #        is_playoff = False
                    if match.played:
                        print("       Not to be played")
                    else:
                        match.play(self.manager.team, match.league.is_playoff)
                    #print (f"{match.home_team.name} - {match.away_team.name}: {match.home_goals} - {match.away_goals}")
            leagues = self.get_leagues_by_type("Normal")
            for league in leagues:
                league.calculate_table()
                if(league.playoff_for_league is not None and league.is_completed()):
                    if(not league.playoff_for_league.is_started):
                        print(f"Time for playoff - {league.playoff_for_league.name} - is_started: {league.playoff_for_league.is_started}")
                        league.playoff_for_league.create_quarter_finals_schedule(league.get_playoff_teams())
            qleagues = self.get_leagues_by_type("Qualification")
            for qleague in qleagues:
                if(qleague.is_started):
                    qleague.calculate_table()
                else:
                    qleague_list = []
                    qleagues_completed = True
                    for league in leagues:
                        if league.qualification_league_up == qleague.name:
                            qleague_list.append(league)
                            if not league.is_completed():
                                qleagues_completed = False
                        if league.qualification_league_down == qleague.name:
                            qleague_list.append(league)
                            if not league.is_completed():
                                qleagues_completed = False
                    if qleagues_completed == True:
                        qteams = []
                        for league in qleague_list:
                            if league.qualification_league_up == qleague.name:
                                qteams += league.get_teams_to_qualification_up()
                            if league.qualification_league_down == qleague.name:
                                qteams += league.get_teams_to_qualification_down()
                        qleague.teams = qteams

            for playoff in self.playoffs:
                playoff.create_semi_schedule_from_quarter()
                playoff.create_final_schedule_from_semi()
                if playoff.is_started:
                    debugprint_playoff(playoff)
            #    for match in playoff.matches:
            #        print(f" * {match.home_team.name} - {match.away_team.name} : {match.home_goals} - {match.away_goals} __ {match.played}")
            #    playoff.check_elimination_quarterfinal()
            isMatchesPlayed = True
        else:
            isMatchesPlayed = False
        self.day += 1
        if self.month in [4, 6, 9, 11]:
            month_days = 30
        elif self.month == 2:
            if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
                month_days = 29
            else:
                month_days = 28
        else:
            month_days = 31

        if self.day > month_days:
            self.day = 1
            self.month += 1

        if self.month > 12:
            self.month = 1
            self.year += 1

        if isMatchesPlayed == True:
            self.game_page = "home"

        return isMatchesPlayed, match_viewed, match_to_view

    def schedule_match(self, match):
        # logic to schedule match goes here
        self.match_manager.add_match(match)

    def quit_game(self):
        # quit game
        pass

