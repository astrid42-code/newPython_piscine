import string


def ft_filter(s, n):

    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items
    that are true.
    """

    res = [s.translate(str.maketrans('', '', string.punctuation))]
    res = ''.join(res)
    x = res.split()
    # list comprehension :
    newlist = [words for words in x if len(words) > n]
    print(newlist)
