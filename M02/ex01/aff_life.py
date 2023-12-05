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

    df = graph['country'] == country
    name = graph['country'].values[0]
    life_expect = df.values[0]

    res = plt.plot([life_expect], [1])
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.show()
    
    
    
#     df = graph.loc[graph['country'] == country] # = ligne pour la France (mais aussi le header?)



#     # print(graph['country'])

#     # print(type(graph['country'])) # > type = series, ie les colonnes d'un dataframe
#     # un data frame a 2 dimensions avec plusieurs colonnes, alors que la Series n’a qu’une seule dimension. 
#     # Une Series ne peut contenir qu’un seul type, alors qu’un data frame, qui est finalement une collection de Series, peut contenir des colonnes de types différents
#     # https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857439-manipulez-le-data-frame

#     # print(df.iloc[0]) # > France et sa data
#     # print(graph.sort_values('country'))
#     # print(df.iloc[0,1:])

#     # print(df.iloc[0:,0:])


#     # print(df.iloc[0][0]) # > France
    
#     x = df

#     x = df.iloc[0,1:]
#     y = df.loc() #df.index > donne le nbr total de lignes dans le doc
#     # print(y) # la ligne de titre : mais comment la recup?
#     plt.plot(x, df)
#     plt.xlabel('Year')
#     plt.ylabel('Life expectancy')
#     plt.axis([1800, 2080, 30, 80])
#     plt.show()

# # https://python.doctor/page-creer-graphiques-scientifiques-python-apprendre

# # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html

# # doc generale sur graphiques (openclassroom):
# # https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7858074-maitrisez-les-bonnes-pratiques-de-la-data-visualisation
