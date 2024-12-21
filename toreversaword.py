# Function to reverse a word using a loop
def reverse_word(word):
    reversed_word = ""  # Initialize an empty string to hold the reversed word
    
    # Loop through the word in reverse order and append each character
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    
    return reversed_word

# Input: Get the word from the user
word = input("Enter a word: ")

# Reverse the word using the function
reversed_word = reverse_word(word)

# Output the reversed word
print(f"The reversed word is: {reversed_word}")
