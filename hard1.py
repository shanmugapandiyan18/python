import re

def isNumber(s: str) -> bool:
    # Regex pattern for valid number
    pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
    
    # Match the string with the regex pattern
    return bool(re.match(pattern, s.strip()))  # Strip spaces for accurate match

# Input: Get the string from the user
s = input("Enter a string: ")

# Output the result
if isNumber(s):
    print("True")
else:
    print("False")
