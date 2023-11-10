from ft_filter import ft_filter
import sys


def main():
    if len(sys.argv) != 3:
        assert False, "the arguments are bad"

    s = str(sys.argv[1])
    try:
        n = int(sys.argv[2])
    except Exception:
        assert False, "the arguments are bad"
    ft_filter(s, n)


if __name__ == "__main__":
    main()
