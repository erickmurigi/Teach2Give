# Question 6: Count Vowels
# Write a program that counts the number of vowels in a sentence

def count_vowels(sentence):
    # Define a set of vowels
    vowels = set("aeiouAEIOU")

    # Count the number of vowels in the sentence
    vowel_count = sum(1 for char in sentence if char in vowels)

    return vowel_count
