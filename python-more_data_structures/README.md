# Python - More Data Structures: Set, Dictionary

Learn more data structures and techniques for better programing and skills on python.

## Concepts from the text on lambda, map, filter, and reduce functions in Python:

### Lambda Functions

 * Lambda functions are small anonymous functions defined using the `lambda` keyword.

 * Syntax: `lambda arguments: expression` which allows you to implement simple functions in a single line without formally defining a function using `def`.
        
    These are especially useful for short, throwaway functions that are not intended to be used repeatedly.

### Map Function

 * The `map(func, seq)` function applies a function `func` to all the items in a sequence `seq`.

 * In Python 3, `map()` returns an iterator, which is more memory efficient than returning a list.

    Common usage includes transforming data. For example, converting temperatures from Celsius to Fahrenheit.

### Filter Function

 * The `filter(function, sequence)` function constructs an iterator from elements of an iterable for which the function returns true.

    It's used to create a list (or other iterable) that contains only items from the original iterable that meet a condition.

### Reduce Function

 * The `reduce(func, seq)` function continually applies the function `func` to the sequence `seq`. It returns a single value.

 * This function is not a built-in function in Python 3 and must be imported from the `functools` module.

    It's useful for performing computations that cumulatively combine all elements of a list into a single result.

### List Comprehensions vs. Lambda, Map, and Filter

 * List comprehensions - are generally more readable and concise when compared to map and filter functions. Python’s preference for list comprehensions reflects the Pythonic guideline of readability and simplicity.

### Controversy and Usage

 * Guido van Rossum, the creator of Python, had proposed removing `reduce()` from the core Python language due to its complexity and limited use cases.

 * Despite initial proposals, lambda, map, and filter remain part of Python due to their utility and popularity, especially among those coming from functional programming backgrounds like Lisp.

### Practical Applications

 * These functions are heavily utilized in data manipulation, cleaning, and transformation tasks, making them popular in data science and web development.

 * They allow for writing cleaner and more Pythonic code, especially when dealing with iterable transformations and operations that require applying a function to multiple elements in an iterable.

## Main files:

The main file are used for test the finctions, is a copy from Holberton exercise. 

## Tasks:

0. [Squared simple](./0-square_matrix_simple.py)

 * Write a function that computes the square value of all integers of a matrix.

1. [Search and replace](./1-search_replace.py)

 * Write a function that replaces all occurrences of an element by another in a new list.

2. [Unique addition](./2-uniq_add.py)

 * Write a function that adds all unique integers in a list (only once for each integer).

3. [Present in both](./3-common_elements.py)

 * Write a function that returns a set of common elements in two sets.

4. [Only differents](./4-only_diff_elements.py)

 * Write a function that returns a set of all elements present in only one set.

5. [Number of keys](./5-number_keys.py)

 * Write a function that returns the number of keys in a dictionary.

6. [Print sorted dictionary](./6-print_sorted_dictionary.py)

 * Write a function that prints a dictionary by ordered keys.

7. [Update dictionary]

 * Write a function that replaces or adds key/value in a dictionary.

8. Simple delete by key

 * Write a function that deletes a key in a dictionary.

9. Multiply by 2

 * Write a function that returns a new dictionary with all values multiplied by 2

10. Best score

 * Write a function that returns a key with the biggest integer value.

11. Multiply by using map

 * Write a function that returns a list with all values multiplied by a number without using any loops.

12. Roman to Integer

 * Create a function def roman_to_int(roman_string): that converts a Roman numeral to an integer.

    Can't use google.

## Advanced: 

