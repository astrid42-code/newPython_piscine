import matplotlib.pyplot as plt

# 1 recuperer la ligne de donnees correspondant a la france (comment?)
# 2 definir x et y avec :
# x = la 1ere ligne de mon csv (sans 1ere colonne)
# y = la ligne de donnees correspondant a la France (sans la 1ere colonne)
# 3 plt.plot(x, y)


def aff_life(graph, country):

    '''
    Function displays the country information of your campus.
    Your graph must have a title and a legend for each axis.
    '''

    if graph is None:
        return print('Error in data')

    res = graph[country:country].transpose()
    res.plot(xlabel='Year', ylabel='Life expectancy',
             title=country+' Life expectancy Projections')

    plt.show()

# un data frame a 2 dimensions avec plusieurs colonnes, alors que la Series n’a qu’une seule dimension.
# Une Series ne peut contenir qu’un seul type, alors qu’un data frame, qui est finalement une collection de Series, peut contenir des colonnes de types différents
# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857439-manipulez-le-data-frame

# # https://python.doctor/page-creer-graphiques-scientifiques-python-apprendre

# # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html

# # doc generale sur graphiques (openclassroom):
# # https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7858074-maitrisez-les-bonnes-pratiques-de-la-data-visualisation
