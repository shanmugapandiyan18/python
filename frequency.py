# Function to calculate the frequency of each element in the list
def count_frequency(lst):
    frequency = {}
    for element in lst:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return frequency

# Input: Get the list from the user
lst = list(map(int, input("Enter the elements of the list separated by spaces: ").split()))

# Calculate the frequency of each element
frequency = count_frequency(lst)

# Output the results
print("Frequency of each element:")
for element, count in frequency.items():
    print(f"{element}: {count}")
