# Question Three: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.
# Examples:
# 8 => returns True
# 6 => returns False

def is_power_of_two(num):
    # Check if the number is greater than 0 and has only one '1' bit in its binary representation
    return num > 0 and (num & (num - 1)) == 0

# Test cases
print(is_power_of_two(8))  # Output: True
print(is_power_of_two(6))  # Output: False
