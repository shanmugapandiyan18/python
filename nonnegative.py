def max_area(height):
    # Initialize pointers
    left = 0
    right = len(height) - 1
    max_area = 0
    
    # Two-pointer approach
    while left < right:
        # Calculate the area between the two lines
        width = right - left
        h = min(height[left], height[right])
        area = width * h
        
        # Update the maximum area found so far
        max_area = max(max_area, area)
        
        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Test the function
n = int(input("Enter the number of lines: "))
height = list(map(int, input("Enter the heights of the lines: ").split()))

print("Maximum area of water that can be contained is:", max_area(height))
