import globals


def init():
    records = (
        ("Team Name", globals.team_name, "Matches", globals.matches),
        ("Goals", globals.goals, "Shots", globals.shots),
        ("Yellow cards", globals.yellow_cards, "Red cards", globals.red_cards),
        ("Defensive duels", globals.defensive_duels, "Offensive duels", globals.offensive_duels),
        ("Avg. possession percent", globals.avg_possession_percent, "Avg. shots", globals.shots),
        ("Avg. def. duels", globals.avg_defensive_duels, "Avg. off. duels", globals.avg_offensive_duels),
        ("Avg. forward passes", globals.avg_forward_passes, "Avg. backwards passes", globals.avg_backwards_passes),
        ("Winrate", globals.percent_winrate, "% duels won", globals.percent_duelswon),
        ("% off. duels won", globals.percent_offensive_duels_won, "% def. duels won", globals.percent_defensive_duels_won),
        ("Goal conversion", globals.percent_goal_conversion, "% succ. touchinBox", globals.successful_touchInBox),
        ("% succ. forward passes", globals.percent_succesful_forward_passes, "% succ. backwards passes", globals.percent_succesful_backwards_passes),
        ("% passess to final third", globals.percent_succesful_passes_tofinalthird, "% succ. long passes", globals.percent_succesful_long_passes)
    )

    return records
