# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Check divisibility from 2 to sqrt(num)
        if num % i == 0:
            return False
    return True

# Function to print all composite numbers between a and b
def print_composite_numbers(a, b):
    for num in range(a, b + 1):
        if num > 1 and not is_prime(num):  # Check if the number is composite
            print(num, end=" ")

# Input: Get the range from the user
a = int(input("Enter the start of the range (a): "))
b = int(input("Enter the end of the range (b): "))

# Call the function to print the composite numbers in the given range
print(f"Composite numbers between {a} and {b} are:")
print_composite_numbers(a, b)
