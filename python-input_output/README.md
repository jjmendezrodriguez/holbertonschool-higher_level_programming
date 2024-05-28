# Python - Input/Output

# Python Programming Overview

This README provides an overview of various Python programming concepts covered, including input/output operations, error and exception handling, and JSON data handling.

## 1. Input and Output in Python

### Fancier Output Formatting

- **Formatted string literals (f-strings)**: Allow embedding expressions inside string literals for inline formatting.

- **str.format()**: Offers extensive functionality for string formatting.

- **Manual String Manipulation**: Using methods like `str.rjust()`, `str.ljust()`, and `str.center()` to align text.

### Working with Files

- **Reading and Writing Files**: Using `open()` function with modes like 'r', 'w', 'a' for reading, writing, and appending respectively.

- **Automatic File Closing**: Using `with` statement for better resource management.

## 2. Errors and Exceptions

### Syntax Errors

- Errors found by the parser when the syntax does not conform to Python rules.

### Exceptions

- Runtime errors detected during execution, like `ZeroDivisionError`, `NameError`, and `TypeError`.

### Handling Exceptions

- Using `try` and `except` blocks to catch and handle exceptions effectively.

- `finally` block for clean-up actions, executed under all circumstances.

## 3. JSON Handling in Python

### Basic Operations

- **json.dumps()**: Serializing Python object hierarchies to JSON strings.

- **json.loads()**: Deserializing JSON strings back into Python objects.

### Advanced JSON Features

- **Custom Encoders and Decoders**: Extending `JSONEncoder` and `JSONDecoder` to handle complex types like complex numbers.

- **Handling Special Types**: Using hooks like `parse_float` to customize parsing of numerical values.

### Security Considerations

- Be cautious when parsing JSON from untrusted sources to avoid security vulnerabilities like excessive CPU and memory consumption.

## Tests files:
    
 This files are made for tests the errors on the code. 

## Mains Files:

 The main file are used for test the finctions, is a copy from Holberton exercise.

 ## Tasks:

0. [Read file](./0-read_file.py)

 * Write a function that reads a text file (`UTF8`) and prints it to stdout.

1. [Write to a file](./1-write_file.py)

 * Write a function that writes a string to a text file (`UTF8`) and returns the number of characters written.

2. [Append to a file]()