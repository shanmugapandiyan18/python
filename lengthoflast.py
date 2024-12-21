def length_of_last_word(s: str) -> int:
    # Strip any trailing spaces and split the string into words
    words = s.strip().split()
    
    # The last word will be the last element in the list
    if words:
        return len(words[-1])
    return 0  # If the string is empty or contains only spaces

# Input: Get the string from the user
s = input("Enter a string: ")

# Get the length of the last word
last_word_length = length_of_last_word(s)

# Output the result
print(f"The length of the last word is: {last_word_length}")
