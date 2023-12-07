import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd


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
    tmp = data[[mycountry, othercountry]].replace(modif_dict, regex=True).map(eval).astype(int)
    # map(eval) > eval for evaluated type value of each cell
    # https://stackoverflow.com/questions/69914296/how-to-find-each-row-and-column-data-type-in-pandas-dataframe-using-apply-map-o
    # replace in a df:
    # https://pandas.pydata.org/pandas-docs/version/0.23.3/generated/pandas.DataFrame.replace.html
    res = tmp.loc['1800':'2050']
    # res = tmp.iloc[0:251, :]
    print(res)
    # erreur dans les axis a corriger
    plot = res.plot(xlabel='Year', ylabel='Population',
             title='Population Projections')

    plt.show()

# def aff_pop(data: pd.DataFrame, versus: str):
#     '''
#     Take a panda dataframe in argument wich discribe all world coutries
#     populations. Transpose the dataframe and display France versus Colombie
#     informations between 1850 and 2050.
#     '''
#     if data is None:
#         return print("The program could not load the data")
#     repl_dict = {'[kK]': '*1e3', '[mM]': '*1e6', '[bB]': '*1e9'}
#     data_transpose = data.T
#     db = data_transpose[["France", versus]].replace(repl_dict, regex=True)\
#         .applymap(eval).astype(int)
#     df_between = db.loc['1850':'2050']
#     df_between.plot(xlabel="Year", ylabel="Population",
#                     title="Population Projections")
#     plt.show()


def main():
    res = load("population_total.csv")
    aff_pop(res, 'France', 'Belgium')
    # aff_pop(res, 'Belgium')


if __name__ == "__main__":
    main()
