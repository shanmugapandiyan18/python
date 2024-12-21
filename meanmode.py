import statistics

# Function to calculate mean, median, and mode
def calculate_statistics(nums):
    # Mean
    mean = sum(nums) / len(nums)

    # Median
    nums_sorted = sorted(nums)
    n = len(nums_sorted)
    if n % 2 == 1:
        median = nums_sorted[n // 2]
    else:
        median = (nums_sorted[n // 2 - 1] + nums_sorted[n // 2]) / 2

    # Mode (using statistics module for simplicity)
    try:
        mode = statistics.mode(nums)
    except statistics.StatisticsError:
        mode = "No unique mode"  # When there is no unique mode

    return mean, median, mode

# Input: List of numbers
nums = list(map(int, input("Enter a list of numbers (space-separated): ").split()))

# Calculate mean, median, and mode
mean, median, mode = calculate_statistics(nums)

# Display the results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
