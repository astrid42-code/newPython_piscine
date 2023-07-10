cf exo ancienne piscine mais attention : rajouter les nombres (isdigit())

import sys

def text_analyzer(str):

    """
    This function takes a single string argument and displays
    the sums of its upper-case characters, lower-case characters, 
    punctuation characters and spaces.
    Then it prints each category
    """

    uc = 0
    lc = 0
    s = 0
    nb = 0
    if len(str) > 0:
        for i in str:
            if i.isupper():
                uc += 1
            elif i.islower():
                lc += 1
            elif i.isspace():
                s += 1
            elif i.isdigit(): 
                nb += 1
        total = len(str)
        # p : punctuation = total nb of chars - analyzed chars - numbers
        p = total - (uc + lc + s) - nb
        aff(total, uc, lc, p, s)

def aff(total, uc, lc, p, s):
    print("The text contains ", total, " character(s):")
    print("- ", uc, " upper letter(s)")
    print("- ", lc, " lower letter(s)")
    print("- ", p, " punctuation mark(s)")
    print("- ", s, " space(s)")

def main():
    if (len(sys.argv) > 2):
        assert False, "ERROR: wrong number of arguments."
    elif (len(sys.argv) == 2):
        text = sys.argv[1]
    else:
        text = input("What is the text to analyze?\n")
    try:
        text_analyzer(text)
    except Exception:
	    assert False, "argument is not a string"

if __name__ == "__main__":
    main()
