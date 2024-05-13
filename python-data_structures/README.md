# Python - Data Structures: Lists, Tuples

## 1. List:
* Basics: Lists are mutable sequences of items of mixed types.
### Methods:
* append(x): Adds an item to the end.
* extend(iterable): Extends list by appending elements from an iterable.
* insert(i, x): Inserts an item at a given position.
remove(x): Removes the first item whose value is x.
* pop([i]): Removes the item at the given position and returns it.
* clear(): Removes all items from the list.
* index(x, [start, [end]]): Returns the index of the first item equal to x.
* count(x): Returns the number of times x appears in the list.
* sort(key=None, reverse=False): Sorts the list in place.
* reverse(): Reverses the list in place.
* copy(): Returns a shallow copy of the list.

## 2. Using Lists as Stacks and Queues
* Stacks: Last-in, first-out behavior. Use append() to push an item and pop() to pop an item.
* Queues: First-in, first-out behavior. For efficiency, use collections.deque.

## 3. List Comprehensions
* Simplify the creation of lists using an expressive and concise syntax.
* Can include conditional expressions.
* Examples include creating lists of squares, filtering based on conditions, and more complex operations like pairing elements of two lists if they aren't equal.

## 4. Tuple
* Basics: Tuples are immutable sequences, typically used for storing heterogeneous data.
* Features: Tuples can be indexed, sliced, and nested. They support packing and unpacking.
* Usage: Commonly used where immutability is required or when returning multiple values from functions.

## 5. Sets
* Basics: Sets are unordered collections of unique elements.
* Operations: Support mathematical operations like union, intersection, difference.
* Use Cases: Useful for membership testing, removing duplicates, and set operations.

## 6. Dictionaries
* Basics: Collections of key-value pairs with unique keys.
* Operations: Keys can be any immutable type. Values are accessed by key, not by position.
* Methods: Include direct access, updates, and removal of key-value pairs.

## 7. Looping Techniques
* Dictionaries: Use items() to loop through key-value pairs.
* Sequences: Use enumerate() to get index and value.
* Parallel Iteration: Use zip() to loop over multiple sequences simultaneously.
* Reversed and Sorted Looping: Use reversed() and sorted() to alter loop order.

## 8. Conditions and Comparisons
* Chained Comparisons: Support for chaining comparisons logically.
* Boolean Operations: Use of and, or, and not for logical operations.
* Comparing Different Types: Python handles type comparisons gracefully, raising exceptions where no natural order exists.

## Main Files

The main files are for test the functions.

## Tasks:

### 0. Print a list of integers

Function that prints all integers from a given list on separate lines using the str.format() method without casting integers into strings directly in the print function.

### 1. Secure access to an element in a list

Function that replaces an element of a list at a specific position, efficiently checks for edge cases involving list indexing and provides a clear, simple approach to element retrieval in lists according to specified rules.

### 2. Replace element

Function effectively guards against out-of-range errors by ensuring that any attempts to modify the list at an invalid index do not alter the list and safely return the original list.

### 3. Print a list of integers... in reverse!

Function prints all integers from a given list in reverse order, you can utilize Python's slicing feature to reverse the list and then iterate over the reversed list to print each integer.

### 4. Replace in a copy

Function new_in_list replaces an element at a specified index without modifying the original list, you need to create a copy of the list within the function.

### 5. Can you C me now?

Function that removes all occurrences of the characters 'c' and 'C' from a string without using the str.replace() method, you can use a list comprehension to filter out these characters and then join the list back into a string. Effectively filters out 'c' and 'C' from the input string and constructs a new string from the remaining characters, meeting the requirement to not use str.replace() and to avoid importing any modules.

### 6. Lists of lists = Matrix

Function that prints a matrix of integers without directly converting integers into strings and without importing any modules, you can use Python's string formatting capabilities provided by the str.format() method.Function is a versatile and straightforward way to print matrices of integers formatted correctly in a typical matrix layout. It follows Python's best practices for function implementation without using any external modules.

### 7. Tuples addition

Function add_tuple that adds the corresponding elements of two tuples according to the provided conditions, you can handle the potential variations in tuple sizes directly within the function.

### 8. More returns!

Function multiple_returns that meets the requirements of returning a tuple containing the length of a string and its first character (or None if the string is empty), you can use conditional expressions to handle the empty string case.

### 9. Find the max

Function max_integer that determines the largest integer in a list without using the built-in max() function and handles the case where the list might be empty, you can iterate through the list manually to find the maximum value.

### 10. Only by 2

Function divisible_by_2 that evaluates each element in a list to determine if it is a multiple of 2, and then returns a new list where each element is either True or False corresponding to the result of this check, you can use a list comprehension.