import math

# Function to find the least number of perfect square numbers that sum to n
def numSquares(n):
    # Initialize a DP array where dp[i] represents the least number of squares that sum up to i
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # 0 can be represented by 0 squares
    
    # Precompute perfect squares less than or equal to n
    perfect_squares = [i * i for i in range(1, int(math.sqrt(n)) + 1)]
    
    # Fill the DP array
    for i in range(1, n + 1):
        for square in perfect_squares:
            if i - square >= 0:
                dp[i] = min(dp[i], dp[i - square] + 1)

    # The value at dp[n] will give the least number of perfect squares
    return dp[n]

# Main function to drive the program
def main():
    # Read user input for n
    n = int(input("Enter an integer n: "))
    
    # Get the least number of perfect square numbers that sum to n
    result = numSquares(n)
    
    print(f"The least number of perfect squares that sum to {n} is: {result}")

# Entry point of the program
if __name__ == "__main__":
    main()
