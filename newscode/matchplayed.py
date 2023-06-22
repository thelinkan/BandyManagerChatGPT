import json
import random

from newscode.newsitem import NewsItem

def matcharticle(game, match, manager_team):
    # Get the first media outlet from the game's media outlets list
    use_mediaoutlet = game.mediaoutlets[0]

    # Determine if the manager's team is the home team or the away team
    if match.home_team.name == manager_team:
        is_manager_home = True
        opponent_name = match.away_team.name
    else:
        is_manager_home = False
        opponent_name = match.home_team.name

    # Load the templates from the JSON file
    with open("data/newstexts/matchresults.json", 'r', encoding='utf-8') as file:
        templates_data = json.load(file)

    # Create the headline and media text based on the match result
    if match.home_goals > match.away_goals:
        if is_manager_home:
            headline = f"{manager_team} won against {opponent_name}"
            templates = templates_data["win_templates"]["firstline_home_team_wins"]
        else:
            headline = f"{manager_team} won away against {opponent_name}"
            templates = templates_data["win_templates"]["firstline_away_team_wins"]
    else:
        if is_manager_home:
            headline = f"{manager_team} lost to {opponent_name}"
            templates = templates_data["loss_templates"]["firstline_home_team_losses"]
        else:
            headline = f"{manager_team} lost away to {opponent_name}"
            templates = templates_data["loss_templates"]["firstline_away_team_losses"]
    template = random.choice(templates)
    # Format the template with the required variables
    #mediatext = template
    mediatext = template.format(manager_team=manager_team, opponent_name=opponent_name,
                                match=match)
    # Create a NewsItem object and add it to the game's news items
    newsitem = NewsItem((game.year, game.month, game.day), headline, mediatext, use_mediaoutlet)
    print(newsitem.text)
    game.newsitems.append(newsitem)
