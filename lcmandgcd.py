import math

# Function to calculate GCD of two numbers
def gcd(a, b):
    return math.gcd(a, b)

# Function to calculate LCM of two numbers
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Function to calculate GCD of n numbers
def gcd_of_n_numbers(nums):
    result = nums[0]
    for num in nums[1:]:
        result = gcd(result, num)
    return result

# Function to calculate LCM of n numbers
def lcm_of_n_numbers(nums):
    result = nums[0]
    for num in nums[1:]:
        result = lcm(result, num)
    return result

# Input: Get n numbers from the user
n = int(input("Enter the number of elements: "))
nums = list(map(int, input(f"Enter {n} numbers separated by spaces: ").split()))

# Calculate GCD and LCM of the list of numbers
gcd_result = gcd_of_n_numbers(nums)
lcm_result = lcm_of_n_numbers(nums)

# Output the results
print(f"The GCD of the given numbers is: {gcd_result}")
print(f"The LCM of the given numbers is: {lcm_result}")
