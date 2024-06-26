# Python - Inheritance

This document provides an overview of class inheritance in Python, explaining the basic concepts and providing examples to illustrate how inheritance is used to extend and modify class behaviors.

## Table of Contents

- [1. Introduction to Inheritance](#1-introduction-to-inheritance)
- [2. Basic Inheritance](#2-basic-inheritance)
- [3. Multiple Inheritance](#3-multiple-inheritance)
- [4. Method Resolution Order (MRO)](#4-method-resolution-order-mro)
- [5. Using `super()`](#5-using-super)
- [6. Practical Examples](#6-practical-examples)

## 1. Introduction to Inheritance

Inheritance is a fundamental concept in object-oriented programming that allows one class to inherit the attributes and methods of another. In Python, all classes implicitly inherit from the `object` class, making them all new-style classes.

## 2. Basic Inheritance

Basic inheritance allows a derived class to inherit properties and methods from a base class. This simplifies code and promotes code reuse.

Example:

        python
        class Animal:
            def __init__(self, name):
                self.name = name

            def speak(self):
                raise NotImplementedError("Subclasses must create this method")

        class Dog(Animal):
            def speak(self):
                return "Woof!"

        class Cat(Animal):
            def speak(self):
                return "Meow!"

## 3. Multiple Inheritance

Python also supports multiple inheritance, allowing a class to inherit from more than one base class.

Example:

        class Father:
            def gardening(self):
                return "I enjoy gardening"

        class Mother:
            def cooking(self):
                return "I love cooking"

        class Child(Father, Mother):
            def hobbies(self):
                return f"{self.gardening()} and {self.cooking()}"

## 4. Method Resolution Order (MRO)

The Method Resolution Order (MRO) determines the order in which Python looks for a method in a hierarchy of classes. It uses the C3 linearization algorithm.

`print(Child.__mro__)`

## 5. Using `super()`

The super() function is used to call methods from a superclass in a subclass, facilitating cooperative multiple inheritance.

Example:

        class Base:
            def __init__(self, name):
                self.name = name

        class Derived(Base):
            def __init__(self, name, age):
                super().__init__(name)
                self.age = age

## 6. Practical Examples
Understanding and utilizing inheritance can simplify the management of large codebases and make the code more modular and maintainable.

        class Bicycle:
            def __init__(self, color, frame_material):
                self.color = color
                self.frame_material = frame_material

        class MountainBike(Bicycle):
            def __init__(self, color, frame_material, front_shock, rear_shock):
                super().__init__(color, frame_material)
                self.front_shock = front_shock
                self.rear_shock = rear_shock

## Tests files:
    
    This files are made for tests the errors on the code. 

## Mains Files:

 The main file are used for test the finctions, is a copy from Holberton exercise.

 ## Tasks:

 0. [Lookup](./0-lookup.py)

  * Write a function that returns the list of available attributes and methods of an object.

1. [My list](./1-my_list.py)

 * Write a class MyList that inherits from list

2. [Exact same object](./2-is_same_class.py)

 * Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

3. [Same class or inherit from](./3-is_kind_of_class.py)

 * Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.

4. [Only sub class of](./4-inherits_from.py)

 * Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.

5. [Geometry module](./5-base_geometry.py)

 * Write an empty class `BaseGeometry`.

6. [Improve Geometry](./6-base_geometry.py)

 * Write a class BaseGeometry (`based on 5-base_geometry.py`).
 
7. [Integer validator](./7-base_geometry.py)

 * Write a class BaseGeometry (`based on 6-base_geometry.py`).

8. [Rectangle](./8-rectangle.py)

 * Write a class Rectangle that inherits from BaseGeometry (`7-base_geometry.py`).

9. [Full rectangle](./9-rectangle.py)

 * Write a class Rectangle that inherits from BaseGeometry (`7-base_geometry.py`). (task based on `8-rectangle.py`)

10. [Square #1](./10-square.py)

 * Write a class Square that inherits from Rectangle (`9-rectangle.py`)

11. [Square #2](./11-square.py)

 * Write a class Square that inherits from Rectangle (`9-rectangle.py`). (task based on `10-square.py)`.

## Advanceds:

12. [My integer](./100-my_int.py)

 * Write a class MyInt that inherits from int.

13. [Can I?](./101-add_attribute.py)

 * Write a function that adds a new attribute to an object if it’s possible.
