def separate_vowels_consonants(input_string):
    vowels = "aeiouAEIOU"  # List of vowels (both lowercase and uppercase)
    consonants = ""
    vowels_str = ""

    # Loop through each character in the input string
    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                vowels_str += char  # Add to vowels string
            else:
                consonants += char  # Add to consonants string

    return vowels_str, consonants


# Input: Get the string from the user
input_string = input("Enter a string: ")

# Get the vowels and consonants
vowels_str, consonants = separate_vowels_consonants(input_string)

# Output the results
print(f"Vowels: {vowels_str}")
print(f"Consonants: {consonants}")
