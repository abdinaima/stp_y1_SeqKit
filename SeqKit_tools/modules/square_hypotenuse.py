
"""This module is called 'square_hypotenuse'.
THe function takes 2 integers, a and b which are the 2 right-angle sides of a triangle.
The function calculates the integer which is the square of the hypotenuse, and prints the outcome."""


def square_hypotenuse (a, b):

    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError ("Both traingle sides must be integers!")
    
    if a < 0 or b < 0:
        raise ValueError ("Both integers must be positive!")

    return a**2 + b**2

if __name__ == "__main__":
    
    print(square_hypotenuse(10, 12))

