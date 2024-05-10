#!/usr/bin/python3
result = ""
for i in range(122, 96, -1):
    char = chr(i)
    if i % 2 == 0:
        result += char.lower()
    else:
        result += char.upper()

print("{}".format(result), end="")
