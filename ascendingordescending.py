# Function to sort names in ascending or descending order
def sort_names(names, order):
    if order == "ascend":
        names.sort()  # Sort names in ascending order
    elif order == "descend":
        names.sort(reverse=True)  # Sort names in descending order
    else:
        print("Invalid choice. Please enter 'ascend' or 'descend'.")

# Main function
def main():
    # Get the list of names from the user
    names = input("Enter a list of names separated by commas: ").split(',')
    names = [name.strip() for name in names]  # Clean extra spaces around names
    
    # Get the sorting order choice from the user
    order = input("Would you like to sort in ascending (ascend) or descending (descend) order? ").lower()
    
    # Call the sort function
    sort_names(names, order)
    
    # Print the sorted list
    print("Sorted list of names:")
    for name in names:
        print(name)

# Run the program
if __name__ == "__main__":
    main()
