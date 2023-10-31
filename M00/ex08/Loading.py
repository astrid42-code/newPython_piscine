# import sys
# from time import time
# verifier si sys autorise ici


def ft_tqdm(lst: range) -> None:

    """
    a faire!
    """
    
    # current = time.time()
    for i in range(len(lst)):
        print('\r')
        print("|%-90s| %d%%" % ('=' * int(90 * i / len(lst)),
              (i + 1) / len(lst) * 100), end='')
        print("[%-20s] %d%%" % ('=' * int(20 * i / len(lst)), (i + 1) / len(lst) * 100), end= '')
        # sys.stdout.write(" | elapsed time %d seconds" % (time.time() - current))
        # sys.stdout.flush()
        yield i
    i += 1


# The '\r' character (carriage return) resets the cursor to the beginning
# of the line and allows you to write over what was previously on the line

# non termine