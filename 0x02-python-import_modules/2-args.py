#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv
    c = len(argv) - 1
    if c == 0:
        print("0 arguments.")
    elif c == 1:
        print("{} argument:".format(c))
        print("{}: {}".format(c, argv[c]))
    elif c > 1:
        print("{} arguments:".format(c))
        for n in range(1, len(argv)):
            print("{}: {}".format(n, argv[n]))
