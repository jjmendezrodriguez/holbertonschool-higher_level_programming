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

## Tasks:

### 0. Print a list of integers

Function that prints all integers from a given list on separate lines using the str.format() method without casting integers into strings directly in the print function.

### 1. Secure access to an element in a list

