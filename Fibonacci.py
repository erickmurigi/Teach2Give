# Question Two: Fibonacci Sequence
# Write a program to generate the Fibonacci sequence up to 100.

# Function to generate Fibonacci sequence
def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence

# Print Fibonacci sequence up to 100
fibonacci_sequence_up_to_100 = generate_fibonacci(100)
print(fibonacci_sequence_up_to_100)
