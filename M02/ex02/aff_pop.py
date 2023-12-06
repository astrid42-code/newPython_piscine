import matplotlib.pyplot as plt
from load_csv import load


def aff_pop(graph, mycountry, othercountry):

    '''
    Function displays the country information of your campus.
    Your graph must have a title and a legend for each axis.
    '''

    if graph is None:
        return print('Error in data')

    print(graph[mycountry:mycountry])

    # change numbers and letters in numeric data for the plot
    # ex : 1e3 = 1000 (10 puissance 3)
    modif = {'[k]': '*1e3', '[M]': '*1e6', '[B]': '*1e9'}
    data = graph.transpose()
    tmp = data[[mycountry, othercountry]].replace(modif, regex=True).map(eval).astype(int)
    # map(eval) > eval for evaluated type value of each cell
    # https://stackoverflow.com/questions/69914296/how-to-find-each-row-and-column-data-type-in-pandas-dataframe-using-apply-map-o
    # replace in a df:
    # https://pandas.pydata.org/pandas-docs/version/0.23.3/generated/pandas.DataFrame.replace.html
    res = tmp.loc['1800':'2050']
    res.plot(xlabel='Year', ylabel='Population',
             title='Population Projections')

    plt.show()


def main():
    res = load("population_total.csv")
    aff_pop(res, 'France', 'Belgium')


if __name__ == "__main__":
    main()
