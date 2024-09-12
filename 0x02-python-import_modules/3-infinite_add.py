#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv
    c = len(argv) - 1
    sum = 0
    if c == 0:
        print(sum)
    else:
        for n in range(1, len(argv)):
            sum += int (argv[n])
        print(sum)
