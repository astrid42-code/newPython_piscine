from load_csv import load
from aff_pop import aff_pop

res = load("population_total.csv")
aff_pop(res, 'France', 'Afghanistan')
