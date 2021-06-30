import json

# Manual variables
name = "FC Schalke 04"
image_path = 'FC_Schalke_04_Logo.png'
# Opening JSON file
f = open('data.json', )

# returns JSON object as
# a dictionary
jsonData = json.load(f)

global team_name
team_name = name
global matches
matches = str(jsonData['total']['matches'])
global goals
goals = str(jsonData['total']['goals'])
global shots
shots = str(jsonData['total']['shots'])
global yellow_cards
yellow_cards = str(jsonData['total']['yellowCards'])
global red_cards
red_cards = str(jsonData['total']['redCards'])
global defensive_duels
defensive_duels = str(jsonData['total']['defensiveDuels'])
global offensive_duels
offensive_duels = str(jsonData['total']['offensiveDuels'])
global avg_possession_percent
avg_possession_percent = str(jsonData['average']['possessionPercent'])
global avg_shots
avg_shots = str(jsonData['average']['shots'])
global avg_defensive_duels
avg_defensive_duels = str(jsonData['average']['defensiveDuels'])
global avg_offensive_duels
avg_offensive_duels = str(jsonData['average']['offensiveDuels'])
global avg_forward_passes
avg_forward_passes = str(jsonData['average']['forwardPasses'])
global avg_backwards_passes
avg_backwards_passes = str(jsonData['average']['backPasses'])
global percent_winrate
percent_winrate = str(jsonData['percent']['win'])
global percent_duelswon
percent_duelswon = str(jsonData['percent']['duelsWon'])
global percent_offensive_duels_won
percent_offensive_duels_won = str(jsonData['percent']['offensiveDuelsWon'])
global percent_defensive_duels_won
percent_defensive_duels_won = str(jsonData['percent']['defensiveDuelsWon'])
global percent_goal_conversion
percent_goal_conversion = str(jsonData['percent']['goalConversion'])
global successful_touchInBox
successful_touchInBox = str(jsonData['percent']['successfulTouchInBox'])
global percent_succesful_forward_passes
percent_succesful_forward_passes = str(jsonData['percent']['successfulForwardPasses'])
global percent_succesful_backwards_passes
percent_succesful_backwards_passes = str(jsonData['percent']['successfulBackPasses'])
global percent_succesful_passes_tofinalthird
percent_succesful_passes_tofinalthird = str(jsonData['percent']['successfulPassesToFinalThird'])
global percent_succesful_long_passes
percent_succesful_long_passes = str(jsonData['percent']['successfulLongPasses'])
global goals_conceded
goals_conceded = str(jsonData['total']['concededGoals'])
global saves
saves = str(jsonData['total']['gkSaves'])
global total_touchinbox
total_touchinbox = str(jsonData['total']['touchInBox'])
global total_crosses
total_crosses = str(jsonData['total']['crosses'])
global percent_successful_crosses
percent_successful_crosses = str(jsonData['percent']['successfulCrosses'])

def get_all_percentages():
    return jsonData['percent']