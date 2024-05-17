def magic_calculation(a, b):
    result = 0
    try:
        for i in range(1, 3):
            if i > a:
                raise Exception("Too far")
            result += (a ** b) / i
    except ValueError:
        result = a + b
    finally:
        print("Inside result:", result)
    return result
