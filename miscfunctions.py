from club import Club
from team import Team

def get_club_from_team(game, team):
    for club in game.clubs:
        for club_team in club.teams:
            if club_team == team:
                return club
    return None