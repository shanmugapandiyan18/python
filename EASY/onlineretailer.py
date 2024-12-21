def calculate_shipping_charge(num_items):
    # If there is only 1 item, the charge is 750
    if num_items == 1:
        return 750
    # For more than 1 item, calculate the charge based on the formula
    else:
        return 750 + (num_items - 1) * 200

def main():
    # Read the number of items from the user
    num_items = int(input("Enter the number of items in the order: "))
    
    # Calculate the shipping charge
    shipping_charge = calculate_shipping_charge(num_items)
    
    # Display the shipping charge, rounded to 2 decimal places
    print(f"The shipping charge is: {shipping_charge:.2f}")

# Entry point of the program
if __name__ == "__main__":
    main()
