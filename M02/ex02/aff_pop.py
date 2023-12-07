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
    modif_dict = {'[k]': '*1e3', '[M]': '*1e6', '[B]': '*1e9'}
    data = graph.transpose()
    tmp = data[[mycountry, othercountry]]\
        .replace(modif_dict, regex=True).map(eval).astype(int)
    # map(eval) > eval for evaluated type value of each cell
    # https://stackoverflow.com/questions/69914296/how-to-find-each-row-and-column-data-type-in-pandas-dataframe-using-apply-map-o
    # replace in a df:
    # https://pandas.pydata.org/pandas-docs/version/0.23.3/generated/pandas.DataFrame.replace.html

    tmp.plot(xlabel='Year', ylabel='Population',
             title='Population Projections')
    plt.axis(ymin=0, ymax=70000000)
    plt.yticks([20000000, 40000000, 60000000], ['20M', '40M', '60M'])
    plt.axis(xmin=0, xmax=250)
    plt.xticks([0, 40, 80, 120, 160, 200, 240],
               ['1800', '1840', '1880', '1920', '1960', '2000', '2040'])
    # a automatiser pour plus de clarte?

    plt.show()


def main():
    res = load("population_total.csv")
    aff_pop(res, 'France', 'Belgium')
    # aff_pop(res, 'Belgium')


if __name__ == "__main__":
    main()
