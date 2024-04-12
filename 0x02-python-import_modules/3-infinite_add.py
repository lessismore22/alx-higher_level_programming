#!/usr/bin/python3
if __name__ == '__main__':

    import sys

    args = sys.argv
    len_args = len(args)
    sum = 0

    if len_args > 1:
        for i in range(1, len_args):
            sum += int(args[i])

    print(sum)
