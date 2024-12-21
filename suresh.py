def sum_of_nth_row(n):
    # The sum of elements in the nth row is 2^n
    return 2 ** n

def main():
    # Input for the row number (n)
    n = int(input("Enter the row number (n): "))
    
    # Calculate the sum of the nth row
    row_sum = sum_of_nth_row(n)
    
    print(f"The sum of the elements in row {n} of Pascal's Triangle is: {row_sum}")

# Run the program
if __name__ == "__main__":
    main()
