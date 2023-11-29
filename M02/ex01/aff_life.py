import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1 recuperer la ligne de donnees correspondant a la france (comment?)
# 2 definir x et y avec :
# x = la 1ere ligne de mon csv (sans 1ere colonne)
# y = la ligne de donnees correspondant a la France (sans la 1ere colonne)
# 3 plt.plot(x, y)


def aff_life(graph, country): # quelle valeur de return?

    '''
    Function displays the country information of your campus.
    Your graph must have a title and a legend for each axis.
    '''

    df = graph.loc[graph['country'] == country] # = ligne pour la France (mais aussi le header?)
    # print(df.iloc[0][0]) > France
    

# https://python.doctor/page-creer-graphiques-scientifiques-python-apprendre

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html
