def max_guests_on_cruise(T, E, L):
    current_guests = 0
    max_guests = 0

    for i in range(T):
        current_guests += E[i]  
        current_guests -= L[i]  
        
        max_guests = max(max_guests, current_guests)
    
    return max_guests

T = 5
E = [7, 0, 5, 1, 3]
L = [1, 2, 1, 3, 4]

print(max_guests_on_cruise(T, E, L))  
