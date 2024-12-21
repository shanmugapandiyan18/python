
text = "   Hello, World!   "
stripped_text = text.strip()
 
print(f"Original: '{text}'")
print(f"Stripped: '{stripped_text}'"),
 
def is_valid_string(s: str) -> bool:
   """
   Checks if the string is valid (non-empty) after stripping whitespace.
 
   Parameters:
       s (str): Input string to validate.
 
   Returns:
       bool: True if the stripped string is not empty, False otherwise.
   """
   stripped_string = s.strip()  
   return bool(stripped_string)  

print(is_valid_string("   "))
print(is_valid_string("Hello"))      
print(is_valid_string("   Hello   ")) 
print(is_valid_string(""))
 
 
 
def is_valid_number(s: str) -> bool:
   """
   Validates if the input string represents a valid number, optionally starting with a '+' or '-'.
 
   Parameters:
       s (str): Input string to validate.
 
   Returns:
       bool: True if the string represents a valid number, False otherwise.
   """
   
   stripped_string = s.strip()
   if not stripped_string:
       return False

   if stripped_string[0] in ('+', '-'):
       stripped_string = stripped_string[1:]  
   
   try:
       float(stripped_string)
       return True
   except ValueError:
       return False