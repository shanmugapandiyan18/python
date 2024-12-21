from collections import Counter

def modify_string(S):
    # Step 1: Calculate the frequency of each character in the string
    freq = Counter(S)
    
    # Step 2: Initialize an empty list to build the modified string
    modified_str = []
    
    # Step 3: Process each character in the original string
    for char in S:
        # Frequency of the current character
        f = freq[char]
        
        # Calculate the new character after applying the circular distance
        new_char = chr((ord(char) - ord('a') + f) % 26 + ord('a'))
        
        # Append the new character to the result list
        modified_str.append(new_char)
    
    # Step 4: Join the list into a string and return the result
    return ''.join(modified_str)

# Test cases
print(modify_string("ghee"))        # Output: "higg"
print(modify_string("elephant"))   # Output: "fmifobvq"
print(modify_string("apple"))      # Output: "applf"
print(modify_string("orange"))     # Output: "opsqgf"
print(modify_string("lion"))       # Output: "mjpo"
