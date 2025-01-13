#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Function description:
    This function computes the factorial of a number n recursively. 
    The factorial of a number n (denoted as n!) is the product of all positive integers 
    less than or equal to n. The base case is when n is 0, where factorial(0) is defined as 1.

    Parameters:
    n (int): A non-negative integer for which we want to compute the factorial.

    Returns:
    int: The factorial of the integer n.
    """
    if n == 0:  # Base case: if n is 0, return 1 (factorial of 0 is 1)
        return 1
    else:
        return n * factorial(n-1)  # Recursive case: n * factorial of (n-1)

# Main execution
f = factorial(int(sys.argv[1]))  # Get the input number from command line argument and calculate its factorial
print(f)  # Print the result
