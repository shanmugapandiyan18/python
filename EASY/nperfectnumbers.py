def find_factors(n, m):
    # Find factors of n and print the first m factors
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
        if len(factors) == m:  # Stop when we've found m factors
            break
    return factors

def is_perfect_number(num):
    # Check if a number is perfect
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num

def find_perfect_numbers(n):
    # Find the first n perfect numbers
    perfect_numbers = []
    num = 2  # Start checking from 2 since 1 is not a perfect number
    while len(perfect_numbers) < n:
        if is_perfect_number(num):
            perfect_numbers.append(num)
        num += 1
    return perfect_numbers

def main():
    # Input the number of perfect numbers and the number of factors
    n = int(input("Enter the number of perfect numbers to find: "))
    m = int(input("Enter the number of factors to display for each perfect number: "))
    
    # Find the first n perfect numbers
    perfect_numbers = find_perfect_numbers(n)
    
    # Print each perfect number and its first m factors
    for num in perfect_numbers:
        print(f"Perfect number: {num}")
        factors = find_factors(num, m)
        print(f"First {m} factors: {', '.join(map(str, factors))}")
        print()

# Entry point of the program
if __name__ == "__main__":
    main()
