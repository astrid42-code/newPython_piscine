import sys

if (len(sys.argv) == 1):
    sys.exit(1)
if (len(sys.argv) > 2):
    assert False, "There are too many arguments"

sys.argv.pop(0)

try:
    nb = int(sys.argv[0])
except Exception:
    assert False, "argument is not an integer"

if nb % 2 == 0 or nb == 0:
    print("I'm Even")
else:
    print("I'm Odd")

sys.exit(1)
