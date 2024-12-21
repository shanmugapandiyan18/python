# Function to calculate bonus and final salary
def calculate_bonus(salary, grade):
    if grade == 'A':
        bonus = salary * 0.05  # 5% bonus for grade A
    elif grade == 'B':
        bonus = salary * 0.10  # 10% bonus for grade B
    else:
        print("Invalid grade entered.")
        return None, None
    
    # Check if salary is less than $10,000 to give an extra 2% bonus
    if salary < 10000:
        bonus += salary * 0.02  # Extra 2% bonus if salary is less than $10,000
    
    # Calculate final salary
    final_salary = salary + bonus
    
    return bonus, final_salary

# Input: Get salary and grade from the user
salary = float(input("Enter the salary of the employee: "))
grade = input("Enter the grade of the employee (A or B): ").upper()  # Ensure the grade is uppercase

# Calculate bonus and final salary
bonus, final_salary = calculate_bonus(salary, grade)

# Output the results if valid
if bonus is not None:
    print(f"The bonus for the employee is: ${bonus:.2f}")
    print(f"The final salary after bonus is: ${final_salary:.2f}")
