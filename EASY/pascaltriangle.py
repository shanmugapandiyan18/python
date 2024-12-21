def generate_pascals_triangle(n):
    # Initialize Pascal's Triangle as a list of lists
    triangle = []
    
    for i in range(n + 1):
        # Start with a row containing just 1
        row = [1] * (i + 1)
        
        # Fill in the values for the middle elements of the row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        # Add the row to the triangle
        triangle.append(row)
    
    return triangle

def sum_of_nth_row(n):
    # Generate Pascal's Triangle up to nth row
    triangle = generate_pascals_triangle(n)
    
    # The sum of the nth row is the sum of its elements
    return sum(triangle[n])

def main():
    # Get the value of n from the user
    n = int(input("Enter the row number (n): "))
    
    # Get the sum of the nth row of Pascal's Triangle
    row_sum = sum_of_nth_row(n)
    
    print(f"The sum of the elements in the {n}th row of Pascal's Triangle is: {row_sum}")

# Entry point of the program
if __name__ == "__main__":
    main()
