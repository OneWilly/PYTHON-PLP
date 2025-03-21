#Task 5: Words with Odd Number of Characters
#Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.


# Task 5: Words with Odd Number of Characters

# Step 1: Create a list of words
words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]

# Step 2: Use list comprehension to filter words with odd lengths
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Step 3: Print the result
print("Words with an odd number of characters:", odd_length_words)
