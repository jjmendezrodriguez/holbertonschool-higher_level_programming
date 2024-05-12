#!/usr/bin/python3
import sys


def main():

    num_args = len(sys.argv) - 1
    if num_args == 0:
        print(f"{num_args} arguments.")
    elif num_args == 1:
        print(f"{num_args} argument:")
    else:
        print(f"{num_args} arguments:")

    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")


if __name__ == "__main__":
    main()
