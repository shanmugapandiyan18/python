# Function to reverse a number using a loop
def reverse_number(n):
    reversed_num = 0
    
    # Loop to reverse the number
    while n > 0:
        # Extract the last digit and add it to the reversed number
        last_digit = n % 10
        reversed_num = reversed_num * 10 + last_digit
        
        # Remove the last digit from the original number
        n = n // 10
    
    return reversed_num

# Input: Get a number from the user
number = int(input("Enter a number: "))

# Call the function to reverse the number
reversed_number = reverse_number(number)

# Output the reversed number
print(f"The reversed number is: {reversed_number}")
