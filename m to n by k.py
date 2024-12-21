# Function to print numbers from M to N with step size K
def print_numbers(M, N, K):
    for number in range(M, N+1, K+1):
        print(number, end=" ")

# Get input from the user in list format
input_data = input("Enter M, N, and K separated by spaces: ").split()

# Convert input data to integers
M = int(input_data[0])
N = int(input_data[1])
K = int(input_data[2])

# Call the function to print numbers
print_numbers(M, N, K)
