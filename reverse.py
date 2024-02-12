# Question Five Reverse Integer
# Write a program that takes an integer as input and returns an integer with reversed digit
# ordering.

def reverse_integer(num):
    # Convert the integer to a string, reverse it, and convert it back to an integer
    reversed_str = str(num)[::-1]
    reversed_num = int(reversed_str)

    # Adjust the sign for negative numbers
    if num < 0:
        reversed_num = -reversed_num

    return reversed_nu
