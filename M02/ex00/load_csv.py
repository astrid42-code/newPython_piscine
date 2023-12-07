import pandas as pd


def load(path: str) -> pd.DataFrame:
    # (You have to adapt the type of return according to your library)

    '''
    This function takes a path as argument, writes the dimensions
    of the data set and returns it
    '''

    if not path.endswith('.csv'):
        return print("CSV only")
    try:
        df = pd.read_csv(path)
        # index_col=0 > begins at the country column
        print("Loading dataset of dimensions", df.shape)
        # The shape attribute returns a two-item tuple of the number of rows and the number of columns in the DataFrame. For a Series, it returns a one-item tuple
    except Exception:
        return print("Unvalid path/file")
    return df
