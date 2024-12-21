def add_binary(a: str, b: str) -> str:
    # Initialize variables
    result = []
    carry = 0
    i, j = len(a) - 1, len(b) - 1
    
    # Loop through both strings from right to left
    while i >= 0 or j >= 0 or carry:
        # Get the current bits (0 if out of range)
        bit_a = int(a[i]) if i >= 0 else 0
        bit_b = int(b[j]) if j >= 0 else 0
        
        # Sum of the bits and the carry
        total = bit_a + bit_b + carry
        
        # Resulting bit is total mod 2, carry is total divided by 2
        result.append(str(total % 2))
        carry = total // 2
        
        # Move to the next bits
        i -= 1
        j -= 1
    
    # Join the result list and reverse it to get the final binary string
    return ''.join(result[::-1])

# Input: Get binary strings a and b from the user
a = input("Enter the first binary string: ")
b = input("Enter the second binary string: ")

# Calculate the sum
sum_binary = add_binary(a, b)

# Output the result
print(f"The sum of {a} and {b} is: {sum_binary}")
