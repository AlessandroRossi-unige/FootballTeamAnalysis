import globals
import numpy as np
from matplotlib import pyplot as plt


def create_piechart(values, name):
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')
    colors = ['#30ba55', '#db3a1a']
    explode = (0.1, 0)
    autotext = ax.pie(values, colors=colors, explode=explode, autopct='%1.2f%%')
    autotext[2][0].set_fontsize(30)
    autotext[2][1].set_fontsize(30)
    path = name + '.png'
    plt.savefig(path)
    return path


def off_duels_won():
    value = float(globals.percent_offensive_duels_won)
    values = [value, 100.0-value]
    name = 'Offensive capability'
    return create_piechart(values, name)


def def_duels_won():
    value = float(globals.percent_succesful_passes_tofinalthird)
    values = [value, 100.0-value]
    name = 'Defensive capability'
    return create_piechart(values, name)


def succ_pass_toFinalThird():
    value = float(globals.percent_succesful_passes_tofinalthird)
    values = [value, 100.0-value]
    name = 'Successful passes to final third'
    return create_piechart(values, name)


def succ_gkSaves():
    value = float(globals.saves)/(float(globals.saves)+float(globals.goals_conceded)) * 100
    values = [value, 100.0-value]
    name = 'Succesfull saves'
    return create_piechart(values, name)


def successful_crosses():
    value = float(globals.percent_successful_crosses)
    values = [value, 100.0-value]
    name = 'Successful crosses'
    return create_piechart(values, name)
