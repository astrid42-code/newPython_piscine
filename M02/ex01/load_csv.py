import pandas as pd


def load(path: str) -> pd.DataFrame:
    # (You have to adapt the type of return according to your library)

    '''
    This function takes a path as argument, writes the dimensions
    of the data set and returns it
    '''

    try:
        open(path, "r")
    except Exception:
        print("Unvalid path/file")
        return

    # autres cas d'erreurs a voir?
    # genre le type est-il bien DataFrame?

    df = pd.read_csv(path)

    # The shape attribute returns a two-item tuple of the number of rows and the number of columns in the DataFrame. For a Series, it returns a one-item tuple
    print("Loading dataset of dimensions", df.shape)
    print(df)
    print(type(df))
    # imprime correctement le tableau mais egalement : [195 rows x 302 columns]
    # a retirer(?)

    # doit on close?
