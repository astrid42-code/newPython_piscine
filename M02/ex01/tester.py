from load_csv import load
from aff_life import aff_life

res = load("life_expectancy_years.csv")
aff_life(res, 'France')
