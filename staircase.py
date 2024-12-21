def climbStairs(n):
    # Base cases
    if n == 0:
        return 1  # There's 1 way to stay at the ground (do nothing)
    elif n == 1:
        return 1  # There's 1 way to climb to the first step
    
    # Variables to store the number of ways to reach the last two steps
    prev1 = 1  # ways(1)
    prev2 = 1  # ways(0)
    
    # Bottom-up calculation
    for i in range(2, n + 1):
        current = prev1 + prev2  # ways(i) = ways(i-1) + ways(i-2)
        prev2 = prev1  # Update prev2 to the previous step
        prev1 = current  # Update prev1 to the current step
    
    return prev1  # The final result is the number of ways to reach step n

# Test the function
n = int(input("Enter the number of steps: "))
print(f"Number of distinct ways to climb {n} steps is: {climbStairs(n)}")
