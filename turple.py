# ==================================================
# TUPLES IN PYTHON
# ==================================================

# A tuple is an ordered, immutable collection of items.
# Tuples are defined using parentheses ().

# Example of a tuple
my_tuple = (1, 2, 3, "Python", 3.14, True)
print("Example tuple:", my_tuple)

# ==================================================
# ACCESSING TUPLE ELEMENTS
# ==================================================

# Tuples are ordered, so you can access elements using their index.
# Python uses zero-based indexing.

fruits = ("apple", "banana", "cherry")
print("\nAccessing tuple elements:")
print("First element:", fruits[0])  # Output: apple
print("Third element:", fruits[2])  # Output: cherry

# Negative indexing allows you to access elements from the end.
print("Last element:", fruits[-1])  # Output: cherry
print("Second last element:", fruits[-2])  # Output: banana

# ==================================================
# TUPLES ARE IMMUTABLE
# ==================================================

# Tuples cannot be modified after creation.
# Uncommenting the line below will raise a TypeError.

# fruits[1] = "blueberry"  # This will raise an error: TypeError

# ==================================================
# COMMON TUPLE OPERATIONS
# ==================================================

# 1. Check if an item exists in a tuple
print("\nChecking if an item exists:")
print("Is 'banana' in fruits?", "banana" in fruits)  # Output: True
print("Is 'grape' in fruits?", "grape" in fruits)   # Output: False

# 2. Get the length of a tuple
print("\nLength of the tuple:")
print("Number of fruits:", len(fruits))  # Output: 3

# 3. Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
combined_tuple = tuple1 + tuple2
print("\nConcatenated tuple:", combined_tuple)  # Output: (1, 2, 3, 'a', 'b', 'c')

# 4. Repeating tuples
repeated_tuple = ("Python",) * 3
print("\nRepeated tuple:", repeated_tuple)  # Output: ('Python', 'Python', 'Python')

# 5. Slicing a tuple
fruits = ("apple", "banana", "cherry", "orange", "mango")
print("\nSlicing a tuple:")
print("Elements from index 1 to 3:", fruits[1:4])  # Output: ('banana', 'cherry', 'orange')
print("First 3 elements:", fruits[:3])           # Output: ('apple', 'banana', 'cherry')
print("Elements from index 2 to end:", fruits[2:])  # Output: ('cherry', 'orange', 'mango')

# ==================================================
# NESTED TUPLES
# ==================================================

# Tuples can contain other tuples, creating a nested structure.
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print("\nNested tuple (matrix):")
print("Element at row 2, column 3:", matrix[1][2])  # Output: 6

# ==================================================
# SINGLE-ELEMENT TUPLES
# ==================================================

# To create a tuple with a single element, include a trailing comma.
single_element_tuple = ("Python",)  # Correct
not_a_tuple = ("Python")           # Incorrect (this is a string)
print("\nSingle-element tuple:")
print("Type of single_element_tuple:", type(single_element_tuple))  # Output: <class 'tuple'>
print("Type of not_a_tuple:", type(not_a_tuple))                   # Output: <class 'str'>

# ==================================================
# CONVERTING BETWEEN LISTS AND TUPLES
# ==================================================

# You can convert a list to a tuple and vice versa.

# List to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print("\nList to tuple:")
print("Converted tuple:", my_tuple)  # Output: (1, 2, 3)

# Tuple to list
my_tuple = (4, 5, 6)
my_list = list(my_tuple)
print("\nTuple to list:")
print("Converted list:", my_list)  # Output: [4, 5, 6]

# ==================================================
# WHEN TO USE TUPLES
# ==================================================

# Use tuples when:
# 1. You want to store data that should not change (e.g., constants).
# 2. You need faster performance (tuples are faster than lists).
# 3. You want to use them as keys in dictionaries (keys must be immutable).

# ==================================================
# KEY POINTS TO REMEMBER
# ==================================================

# 1. Tuples are ordered and immutable.
# 2. They can store heterogeneous data types.
# 3. Use indexing ([index]) to access elements and slicing ([start:end]) to extract subtuples.
# 4. Tuples are faster and more memory-efficient than lists for fixed data.

# ==================================================
# END OF TUPLES DEMO
# ==================================================