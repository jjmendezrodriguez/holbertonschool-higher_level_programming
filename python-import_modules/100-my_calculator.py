#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit


def main():
    for i in argv:
        pass
    if len(argv) != 4 and not isinstance(int(i), int):
        print("Usage: ./100-mycalculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    if len(argv[2]) != 1 and argv[2] not in ['+', '-', '/']:
        operator = chr(42)
    else:
        operator = argv[2]
    b = int(i)

    result = 0
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == chr(42):
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, and /")
        exit(1)

    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    main()
