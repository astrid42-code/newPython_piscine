cf ancienne piscine

import sys
import time

def ft_progress(lst):
    current = time.time()
    for i in range(len(lst)):
        sys.stdout.write('\r')
        sys.stdout.write("[%-20s] %d%%" % ('=' * int(20 * i / len(lst)), (i + 1) / len(lst) * 100))
        sys.stdout.write(" | elapsed time %d seconds" % (time.time() - current))
        sys.stdout.flush()
        yield i
    i += 1

def main():
    listy = range(420)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)

if __name__ == "__main__":
    main()

sys.exit(1)

#The '\r' character (carriage return) resets the cursor to the beginning of the line and allows you to write over what was previously on the line