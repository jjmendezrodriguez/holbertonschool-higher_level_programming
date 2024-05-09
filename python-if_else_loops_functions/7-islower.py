#!/usr/bin/python3
def islower(c):
    if isinstance(c, int):
        raise Exception
    for i in range(97, 123):
        if i == ord(str(c)):
            return True
    return False
