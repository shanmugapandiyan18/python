def print_pattern(starting_number, max_lines):
    # Loop through each line
    for i in range(1, max_lines + 1):
        # Print the number i times, each time starting_number + i - 1
        print(" ".join([str(starting_number + (i - 1))] * i))

def main():
    # Take input from user
    starting_number = float(input("Enter the starting number: "))
    max_lines = int(input("Enter the max number of lines: "))
    
    # Print the pattern
    print_pattern(starting_number, max_lines)

# Entry point of the program
if __name__ == "__main__":
    main()
