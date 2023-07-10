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

# expected output:
# > python whatis.py 14
# I'm Even.
# $>
# $> python whatis.py -5
# I'm Odd.
# $>
# $> python whatis.py
# $>
# $> python whatis.py 0
# I'm Even.
# $>
# $> python whatis.py Hi!
# AssertionError: argument is not an integer
# $>
# $> python whatis.py 13 5
# AssertionError: more than one argument is provided
# $>