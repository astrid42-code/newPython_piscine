from typing import Any


def ft_mean(args: list[int | float]) -> float:
    '''Method to calculate mean of tuple args'''

    len_res = len(args)
    res = 0
    for indice, value in enumerate(args):
        res += value
    res = res / len_res
    return (res)


def ft_median(args: list[int | float]) -> int:
    '''Method to calculate median of tuple args'''

    tmp = sorted(args)
    res = (tmp[int(len(args) / 2)])
    return (res)


def ft_quartile(args: list[int | float]):
    '''Method to calculate quartile[0.25, 0.75] of tuple args'''

    tmp = sorted(args)
    res = [float(tmp[int(len(args) / 4)]), float(tmp[int(3 * len(args) / 4)])]
    return (res)


def ft_std(args: list[int | float]):
    '''Method to calculate standard deviation of tuple args
    The Standard Deviation is a measure of how spread out numbers are.
    To do calculation : do square root of the variance'''

    res = ft_var(args) ** 0.5
    return (res)


def ft_var(args: list[int | float]):
    '''Method to calculate variance of tuple args
    The average of the squared differences from the Mean'''

    len_res = len(args)
    mean = ft_mean(args)
    res = 0
    for indice, value in enumerate(args):
        res += (value-mean)*(value-mean)
    res = res / len_res
    return (res)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    '''function takes in *args a quantity of unknown number
    and make the Mean, Median, Quartile (25% and 75%),
    Standard Deviation and Variance according to the **kwargs ask.'''

    # handling errors :

    # print("size=", len(set(args)), "args = ",args)
    # print("size=", len(set(kwargs)), "kwargs = ", kwargs)
    # print("type : ", type(args), " ", type(kwargs))

    if (args):
        tmp = type(args[0])

    if (args and kwargs):
        for i in args:
            count = type(i)
            # print("count = ", count)
            if (tmp != count):
                return print("Error : elements must be of the same type")

            if isinstance(i, int | float) is False:
                return print("There is an error in args")
        for i in kwargs:
            # print("i=",i, " ", isinstance(i, str))
            if isinstance(i, str) is False:
                return print("There is an error in kwargs")
        # faire des if dans un premier temps en fct du mot cle des kwargs
        # puis encapsuler avec un dico/une liste (comme dans M00)
        VALUES = ["mean", "median", "quartile", "std", "var"]
        # DICT_FT = {mean='ft_mean', median='ft_median', quartile='ft_quartile', std='ft_std', var='ft_var'}

        for key, value in kwargs.items():
            if value not in VALUES:
                pass
            else:
                if value == 'mean':
                    res = ft_mean(args)
                elif value == 'median':
                    res = ft_median(args)
                elif value == 'quartile':
                    res = ft_quartile(args)
                elif value == 'std':
                    res = ft_std(args)
                elif value == 'var':
                    res = ft_var(args)
                print(f'{value} : ', res)
                # print(f'{value} : ', DICT_FT.value(args))
                # en prevoyant un if else au cas ou ce qui est envoye n'est pas dans le dico?
                # ou inutile car deja verifie avant?
                # faire une variable res qui fait appel a une methode en fct du type de calcul
                # en fct de la value demandee (ex mean = add tous les elements puis diviser par le total, ...)
    else:
        for key, value in kwargs.items():
            print("ERROR")


# *args et **kwargs
# https://deusyss.developpez.com/tutoriels/Python/args_kwargs/
