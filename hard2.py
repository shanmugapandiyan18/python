def is_valid_number(s: str) -> bool:
   """
   Validates if the input string represents a valid number, optionally starting with a '+' or '-'.
 
   Parameters:
       s (str): Input string to validate.
 
   Returns:
       bool: True if the string represents a valid number, False otherwise.
   """
   # Strip leading and trailing whitespace
   stripped_string = s.strip()
   
   # Check if the string is empty after stripping
   if not stripped_string:
       return False
   
   # Check for an optional sign at the start
   if stripped_string[0] in ('+', '-'):
       stripped_string = stripped_string[1:]  # Remove the sign for further validation
   
   # Check if the remaining string is a valid number
   try:
       float(stripped_string)
       return True
   except ValueError:
       return False
 
# Accepting input from the user
user_input = input("Enter a value to test if it's a valid number: ")
 
# Test the input
if is_valid_number(user_input):
   print(f"'{user_input}' is a valid number.")
else:
   print(f"'{user_input}' is not a valid number.")