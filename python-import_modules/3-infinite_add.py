#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum_of_args = 0

    for arg in sys.argv[1:]:
        sum_of_args += int(arg)
    print(sum_of_args)
