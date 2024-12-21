def count_characters():
    # Initialize counters for uppercase, lowercase, and numbers
    uppercase_count = 0
    lowercase_count = 0
    number_count = 0
    
    print("Enter characters one by one. Type '*' to stop.")
    
    # Loop to read characters one by one until '*' is encountered
    while True:
        char = input("Enter a character: ")
        
        if char == '*':
            break
        
        # Check if the character is an uppercase letter
        if char.isupper():
            uppercase_count += 1
        # Check if the character is a lowercase letter
        elif char.islower():
            lowercase_count += 1
        # Check if the character is a digit
        elif char.isdigit():
            number_count += 1
        else:
            print("Invalid character. Please enter only letters or digits.")
    
    # After '*' is encountered, display the counts
    print(f"Number of uppercase letters: {uppercase_count}")
    print(f"Number of lowercase letters: {lowercase_count}")
    print(f"Number of digits: {number_count}")

# Entry point of the program
if __name__ == "__main__":
    count_characters()
