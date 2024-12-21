# Function to calculate the number of non-teaching staff
def calculate_non_teaching_staff(staff_users):
    return staff_users // 3  # For every 3 staff, 1 non-teaching staff

# Input: Number of student users, staff users
students = int(input("Enter the number of student users: "))
staff = int(input("Enter the number of staff users: "))

# Calculate the number of non-teaching staff based on staff users
non_teaching_staff = calculate_non_teaching_staff(staff)

# Calculate total users (students + staff + non-teaching staff)
total_users = students + staff + non_teaching_staff

# Display the results
print(f"\nCollege Details:")
print(f"Number of student users: {students}")
print(f"Number of staff users: {staff}")
print(f"Number of non-teaching staff users (based on staff count): {non_teaching_staff}")
print(f"Total number of users in the college: {total_users}")
