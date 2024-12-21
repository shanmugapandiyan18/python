def are_isomorphic(s, t):
    # Check if lengths are different
    if len(s) != len(t):
        return False
    
    # Dictionaries to store the character mappings
    s_to_t = {}
    t_to_s = {}
    
    # Iterate through both strings
    for char_s, char_t in zip(s, t):
        # Check if there is an existing mapping from s to t
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t
        
        # Check if there is an existing mapping from t to s (ensuring the reverse mapping)
        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            t_to_s[char_t] = char_s
    
    return True

# Test the function
s = input("Enter string s: ")
t = input("Enter string t: ")

if are_isomorphic(s, t):
    print("The strings are isomorphic.")
else:
    print("The strings are not isomorphic.")
