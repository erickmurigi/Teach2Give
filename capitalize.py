# Question Four: Capitalize words
# Write a program that accepts a string as input, capitalizes the first letter of each word in the
# string, and then returns the result string.

def capitalize_words(input_str):
    words = input_str.split()
    capitalized_words = [word.capitalize() for word in words]
    result_str = ' '.join(capitalized_words)
    return result_str

# Test cases
print(capitalize_words("hi"))  # Output: "Hi"
print(capitalize_words("i love programming"))  # Output: "I Love Programming"
