import sys
import string

if len(sys.argv) != 3:
    assert False, "wrong number of arguments."

s = str(sys.argv[1])
try:
    n = int(sys.argv[2])
except Exception:
    assert False, "ERROR"


def filter():

    """

    """
    
    res = [s.translate(str.maketrans('', '', string.punctuation))]
    res = ''.join(res)
    x = res.split()
    # list comprehension :
    newlist = [words for words in x if len(words) > n]
    print(newlist)


filter()

sys.exit(1)
