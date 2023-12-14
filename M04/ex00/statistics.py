from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    '''function takes in *args a quantity of unknown number
    and make the Mean, Median, Quartile (25% and 75%),
    Standard Deviation and Variance according to the **kwargs ask.'''

    # handling errors :
    # int min et max?
    # int only?
    # tjrs le meme type dans la liste


    # print(args)
    # print(" ", kwargs)
    if (args and kwargs):
        # print("ouais")
        # faire des if dans un premier temps en fct du mot cle des kwargs
        # puis encapsuler avec un dico/une liste (comme dans M00)
        VALUES = ["mean", "median", "quartile", "std", "var"]
        
        for key, value in kwargs.items():
            if value not in VALUES:
                # print("out")
                pass
            else:
                print(f'{value} : ')
                # faire une variable res qui fit un type de calcul en fct de la value demandee (ex mean = add tous les elements puis diviser par le total, ...) 

            # print("keys = ", key)
            # print("values = ", value)
            

    else:
        print("ERROR")


# *args et **kwargs
# https://deusyss.developpez.com/tutoriels/Python/args_kwargs/
