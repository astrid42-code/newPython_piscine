from load_csv import load
import matplotlib.pyplot as plt


def projection(df1, df2):
    '''
    This function displays the projection of life expectancy in relation
    to the gross national product of the year 1900 for each country.
    '''

    # handling errors
    if df1 is None or df2 is None:
        return print('Error in data')
    data_gross = df1['1900']
    data_life = df2['1900']
    
    plt.scatter(data_gross, data_life)
    plt.title('1900')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life expectancy')
    plt.axis(xmin=300, xmax=11000)
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ['300', '1K', '10K'])
    plt.show()


def main():
    df1 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df2 = load("life_expectancy_years.csv")
    projection(df1, df2)


if __name__ == "__main__":
    main()
