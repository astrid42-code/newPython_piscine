import pandas as pd


def load(path: str): # -> DataFrame:
# (You have to adapt the type of return according to your library)

    '''
    This function takes a path as argument, writes the dimensions
    of the data set and returns it
    '''

    df = pd.read_csv(path)

    # The shape attribute returns a two-item tuple of the number of rows and the number of columns in the DataFrame. For a Series, it returns a one-item tuple
    print("Loading dataset of dimensions", df.shape)
