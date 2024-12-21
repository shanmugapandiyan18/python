def find_averages():
    # Initialize variables to keep track of positive and negative numbers
    positive_numbers = []
    negative_numbers = []
    
    print("Enter numbers one by one. Type '-1' to stop.")
    
    # Loop to read numbers until -1 is encountered
    while True:
        num = float(input("Enter a number: "))
        
        # Stop reading if -1 is encountered
        if num == -1:
            break
        
        # Categorize the number into positive or negative
        if num > 0:
            positive_numbers.append(num)
        elif num < 0:
            negative_numbers.append(num)
    
    # Compute the average of positive numbers, if any
    if positive_numbers:
        positive_average = sum(positive_numbers) / len(positive_numbers)
        print(f"Average of positive numbers: {positive_average:.2f}")
    else:
        print("No positive numbers entered.")
    
    # Compute the average of negative numbers, if any
    if negative_numbers:
        negative_average = sum(negative_numbers) / len(negative_numbers)
        print(f"Average of negative numbers: {negative_average:.2f}")
    else:
        print("No negative numbers entered.")

# Entry point of the program
if __name__ == "__main__":
    find_averages()
