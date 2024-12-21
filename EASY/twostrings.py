def matches(str1, str2):
    # Initialize a counter to count the number of matches
    match_count = 0
    
    # Determine the minimum length to avoid index errors in case strings have different lengths
    min_length = min(len(str1), len(str2))
    
    # Iterate through the characters of both strings
    for i in range(min_length):
        if str1[i] == str2[i]:
            match_count += 1
    
    return match_count

# Example usage
if __name__ == "__main__":
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    
    result = matches(str1, str2)
    print(f"The number of matches between the two strings is: {result}")
