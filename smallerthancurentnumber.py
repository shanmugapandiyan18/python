def smaller_numbers_than_current(nums):
    result = []
    
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[j] < nums[i] and i != j:
                count += 1
        result.append(count)
    
    return result

# Example usage
nums = [8, 1, 2, 2, 3]
print(smaller_numbers_than_current(nums))
