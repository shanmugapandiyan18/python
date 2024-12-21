def is_mirror_number(num_str):
    # Reverse the input string
    reversed_num_str = num_str[::-1]
    
    # Check if the reversed number is equal to the original number
    if num_str == reversed_num_str:
        return True
    else:
        return False

def main():
    # Read the number as a string
    num_str = input("Enter a number: ").strip()
    
    # Check if the number is a mirror number
    if is_mirror_number(num_str):
        print("Yes, it is a Mirror number.")
    else:
        print("No, it is not a Mirror number.")
        
# Entry point of the program
if __name__ == "__main__":
    main()
