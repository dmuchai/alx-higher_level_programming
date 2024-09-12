#!/usr/bin/python3
import sys

def main():
    count_args = len(sys.argv) - 1

    if count_args == 0:
        print("0 arguments.")
    elif count_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count_args))

    for c in range(1, count_args + 1):
        print("{}: {}".format(c, sys.argv[c]))
if __name__ == "__main__":
    main()
