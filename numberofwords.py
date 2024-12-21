# Function to count vowels in a string
def count_vowels(input_string):
    vowels = "aeiouAEIOU"  # List of vowels (both lowercase and uppercase)
    count = 0

    # Loop through each character in the string
    for char in input_string:
        if char in vowels:
            count += 1  # Increment count if the character is a vowel
    
    return count

# Input string
input_string = input("Enter a string: ")

# Call the function and display the result
vowel_count = count_vowels(input_string)
print(f"The number of vowels in the given string is: {vowel_count}")
