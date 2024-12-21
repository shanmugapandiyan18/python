# Function to calculate square and cube of a number
def calculate_square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube

# Input: decimal number
decimal_number = float(input("Enter a decimal number: "))

# Calculate square and cube
square, cube = calculate_square_and_cube(decimal_number)

# Display the results
print(f"The square of {decimal_number} is: {square}")
print(f"The cube of {decimal_number} is: {cube}")
