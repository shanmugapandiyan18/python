import math

def factorial(n):
    # Calculate the factorial of n using a simple loop
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def count_factors(n):
    # Calculate the number of factors of n
    factors_count = 0
    # Only loop through numbers up to sqrt(n)
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i == n // i:
                factors_count += 1  # i and n/i are the same when i is the square root of n
            else:
                factors_count += 2  # i and n/i are different
    return factors_count

def main():
    # Read the number n from the user
    n = int(input("Enter a number: "))
    
    # Calculate and print the factorial of n
    fact = factorial(n)
    print(f"The factorial of {n} is: {fact}")
    
    # Calculate and print the number of factors of n
    factors = count_factors(n)
    print(f"The number of factors of {n} is: {factors}")

# Entry point of the program
if __name__ == "__main__":
    main()
