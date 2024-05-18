# Python - Classes and Objects

## Overview
This README provides a summary of key concepts in Python's object-oriented programming (OOP), focusing on class and instance attributes, and how Python handles data encapsulation and abstraction through properties and traditional getter-setter methods.

## Concepts

### Classes and Instances
- **Class**: A blueprint for creating objects. Classes encapsulate data for the object.
- **Instance**: A specific object created from a class.

### Attributes and Methods
- **Class Attribute**: Attributes that are shared among all instances of a class.
- **Instance Attribute**: Attributes that are specific to an instance.
- **Methods**: Functions defined inside the body of a class and used to define the behaviors of an instance.

### Access Modifiers
- **Public Attributes**: Can be accessed from inside and outside of a class.
- **Protected Attributes** (`_name`): Should not be accessed outside the class, except in a subclass.
- **Private Attributes** (`__name`): Cannot be accessed directly from outside the class.

### Special Methods
- **`__init__`**: Known as the constructor in other OOP languages, used to initialize the instance's attributes.
- **`__str__` and `__repr__`**: Special methods used to define the object's string representation.

### Properties vs. Getters/Setters
- **Property**: Pythonic way to use getters and setters without explicitly defining them, making it easy to add logic later without changing the class interface.
- **Getter and Setter Methods**: Traditional methods used for retrieving and setting values with added logic for data validation.

### Advantages of Properties
- Simplifies access to an attribute with logic behind the scenes.
- Protects the backing data.
- Does not require method calls for access, uses simple attribute access.

### Use Cases for Getters/Setters
- When interfacing with external libraries that expect this kind of structure.
- When transitioning from other languages that heavily use getters/setters, maintaining a familiar structure for those developers.

## Best Practices
- Start with public attributes and migrate to properties if and when necessary for encapsulation and validation without changing the class interface.
- Prefer properties over getters and setters to maintain Pythonic and clean code.

## Examples
Here are simple examples to illustrate class structure and property usage in Python:

python
        class User:
            def __init__(self, name=None):
                self._name = name  # Protected attribute

            @property
            def name(self):
                return self._name

            @name.setter
            def name(self, value):
                if not isinstance(value, str):
                    raise ValueError("Name must be a string")
                self._name = value

        # Usage
        user = User("John Doe")
        print(user.name)  # Access like a regular attribute
        user.name = "Jane Doe"
## Mains Files:

 The main file are used for test the finctions, is a copy from Holberton exercise.

## Task:

0. [My first square](./0-square.py)

 * Write a class Square that defines a square by: (based on `0-square.py`)

1. [Square with size](./1-square.py)

 * Write a class Square that defines a square by: (based on `0-square.py`)

2. [Size validation](./2-square.py)

 * Write a class Square that defines a square by: (based on 1-square.py)

3. [Area of a square](./3-square.py)

 * Write a class Square that defines a square by: (based on `2-square.py`)

4. [Access and update private attribute](./4-square.py)

 * Write a class Square that defines a square by: (based on `3-square.py`)

5. [Printing a square](./5-square.py)

 * Write a class Square that defines a square by: (based on `4-square.py`)

6. [Coordinates of a square](./6-square.py)

 * Write a class Square that defines a square by: (based on `5-square.py`)

## Advanced:

7. [Singly linked list](./100-singly_linked_list.py)

 * Write a class `Node` that defines a node of a singly linked list And, write a class SinglyLinkedList that defines a singly linked list

8. [Print Square instance](./101-square.py)

 * Write a class Square that defines a square by: (based on `6-square.py`)

9. [Compare 2 squares](./102-square.py)

 * Write a class Square that defines a square by: (based on `4-square.py`)

