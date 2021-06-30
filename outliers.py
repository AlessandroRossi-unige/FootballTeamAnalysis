import globals

min_value = 30
max_value = 95


def calculate_outliers():
    return {k:v for (k,v) in globals.get_all_percentages().items() if v > max_value or v < min_value}
