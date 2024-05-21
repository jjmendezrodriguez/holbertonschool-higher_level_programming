# Python - Test-driven development

## Introduction

This document provides an overview of test-driven development (TDD) practices within Python programming. It highlights the importance of using tests, particularly `doctest` and `unittest`, to ensure code reliability and functionality as per the documentation.

## Test-Driven Development (TDD)

Test-driven development is an iterative development process where requirements are turned into very specific test cases, then the software is improved to pass the new tests. This is opposed to software being developed first and test cases created later. Python supports TDD with various tools and libraries.

## Tools for TDD in Python

### Doctest

The `doctest` module searches for pieces of text that look like interactive Python sessions inside docstrings and then executes those sessions to verify that they work exactly as shown.

**Example of a simple doctest in a function:**

        python
        def add(a, b):
            """
            Adds two numbers and returns the result.

            >>> add(2, 3)
            5
            """
            return a + b

        if __name__ == "__main__":
            import doctest
            doctest.testmod()

### Unittest

Unittest is another Python module that is used for writing and running tests. It is more comprehensive than doctest.

**Example of a simple unittest:**

        import unittest

        class TestAddFunction(unittest.TestCase):
            def test_add(self):
                result = add(2, 3)
                self.assertEqual(result, 5)

        if __name__ == '__main__':
            unittest.main()

### Best Practices

 * Document Your Tests: Alongside each function or method, write docstrings to explain what the function does, including examples that can be tested with `doctest`.
 
 * Modular Code: Write code that is modular, making it easier to write tests for each component.

 * Run Tests Frequently: Run your tests frequently to catch regressions or errors as early as possible.

 * Use Continuous Integration (CI): Implement continuous integration to automate tests each time changes are pushed to your version control system.

## Tests files:
    
    This files are made for tests the errors on the code. 

## Mains Files:

 The main file are used for test the finctions, is a copy from Holberton exercise.

 ## Tasks:

0. [Integers addition](./0-add_integer.py)
       
 * Write a function that adds 2 integers.

1. [Divide a matrix](./2-matrix_divided.py)

 * Write a function that divides all elements of a matrix.

2. [Say my name](./3-say_my_name.py)

 * Write a function that prints `My name is <first name> <last name>`

3. [Print square](./3-say_my_name.py)

 * Write a function that prints a square with the character `#`.

4. [Text indentation](./4-print_square.py)

 * Write a function that prints a text with 2 new lines after each of these characters:` ., ? and :`

