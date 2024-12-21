# Function to print the pattern
def print_pattern(rows):
    for i in range(1, rows + 1):
        # Print each row
        for j in range(1, i + 1):
            # Print the value (0.1 * j) with space
            print(f"{0.1 * j}", end=" ")
        # Move to the next line after each row
        print()

# Input: Number of rows
rows = int(input("Enter the number of rows: "))

# Call the function to print the pattern
print_pattern(rows)
