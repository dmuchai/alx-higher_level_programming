#!/usr/bin/python3
if __name__ == "__main__":
    """print the no. and value of CLD"""
    import sys

    count_args = len(sys.argv) - 1

    if count_args == 0:
        print("0 arguments.")
    elif count_args == 1:
        print("{} argument:".format(count_args))
        print("{}: {}".format(count_args, argv[count_args]))
    else:
        print("{} arguments:".format(count_args))
        for c in range(1, count_args + 1):
            print("{}: {}".format(c, sys.argv[c]))