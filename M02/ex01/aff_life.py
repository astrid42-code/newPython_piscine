import matplotlib.pyplot as plt
from load_csv import load


def aff_life(graph, country):

    '''
    Function displays the country information of your campus.
    Your graph must have a title and a legend for each axis.
    '''

    if graph is None:
        return print('Error in data')

    # print(graph[country:country])
    res = graph[country:country].transpose()
    res.plot(xlabel='Year', ylabel='Life expectancy',
             title=country+' Life expectancy Projections')
    plt.axis(xmin=0, xmax=290)
    plt.xticks([0, 40, 80, 120, 160, 200, 240, 280],
               ['1800', '1840', '1880', '1920', '1960',
                '2000', '2040', '2080'])
    # print(res)
    plt.show()


def main():
    res = load("life_expectancy_years.csv")
    aff_life(res, 'France')


if __name__ == "__main__":
    main()

# un data frame a 2 dimensions avec plusieurs colonnes, alors que la Series n’a qu’une seule dimension.
# Une Series ne peut contenir qu’un seul type, alors qu’un data frame, qui est finalement une collection de Series, peut contenir des colonnes de types différents
# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857439-manipulez-le-data-frame

# # https://python.doctor/page-creer-graphiques-scientifiques-python-apprendre

# # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html

# # doc generale sur graphiques (openclassroom):
# # https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7858074-maitrisez-les-bonnes-pratiques-de-la-data-visualisation
