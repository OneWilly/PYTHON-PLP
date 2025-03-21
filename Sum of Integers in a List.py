#Task 1: Sum of Integers in a List
#Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.


# Task 1: Sum of Integers in a List

# Step 1: Accept user input to create a list of integers
numbers = input("Enter a list of integers separated by spaces: ").split()

# Step 2: Convert the input strings to integers
numbers = [int(num) for num in numbers]

# Step 3: Compute the sum of the integers
total_sum = sum(numbers)

# Step 4: Print the result
print("The sum of the integers is:", total_sum)