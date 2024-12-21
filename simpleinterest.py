
principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time period (in years): "))
is_senior_citizen = input("Is the customer a senior citizen? (yes/no): ").strip().lower() == 'yes'

if is_senior_citizen:
    rate_of_interest = 12  
else:
    rate_of_interest = 10  


simple_interest = (principal * rate_of_interest * time) / 100


print(f"The calculated simple interest is: {simple_interest}")
