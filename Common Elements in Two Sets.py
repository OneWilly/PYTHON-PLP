#Task 4: Common Elements in Two Sets
#Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.


# Task 4: Common Elements in Two Sets

# Step 1: Accept user input for the first set of integers
set1 = set(map(int, input("Enter the first set of integers separated by spaces: ").split()))

# Step 2: Accept user input for the second set of integers
set2 = set(map(int, input("Enter the second set of integers separated by spaces: ").split()))

# Step 3: Find the common elements
common_elements = set1.intersection(set2)

# Step 4: Print the result
print("Common elements in both sets:", common_elements)