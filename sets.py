# ==================================================
# PYTHON SETS
# ==================================================

# A set is a collection of unique data. Elements of a set cannot be duplicated.
# Sets are unordered, unindexed, and mutable.

# ==================================================
# CREATING A SET IN PYTHON
# ==================================================

# We create sets by placing all elements inside curly braces {}, separated by commas.
# A set can have any number of items of different types (integer, float, string, etc.).
# However, a set cannot have mutable elements like lists, sets, or dictionaries as its elements.

# Example: Creating different types of sets
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
mixed_set = {1, "apple", 3.14, True}

print("Set of fruits:", fruits)
print("Set of numbers:", numbers)
print("Mixed set:", mixed_set)

# Note: When you run this code, the output order may vary because sets are unordered.

# ==================================================
# CREATING AN EMPTY SET
# ==================================================

# Empty curly braces {} create an empty dictionary, not a set.
# To create an empty set, use the set() function.

empty_set = set()
empty_dictionary = {}

print("\nType of empty_set:", type(empty_set))        # Output: <class 'set'>
print("Type of empty_dictionary:", type(empty_dictionary))  # Output: <class 'dict'>

# ==================================================
# DUPLICATE ITEMS IN A SET
# ==================================================

# Sets automatically remove duplicate items.
duplicate_set = {1, 2, 3, 3, 4, 4, 5}
print("\nSet with duplicates removed:", duplicate_set)  # Output: {1, 2, 3, 4, 5}

# ==================================================
# ADDING AND UPDATING SET ITEMS
# ==================================================

# Sets are mutable, but they are unordered, so indexing has no meaning.
# We cannot access or change an element using indexing or slicing.

# Add an item to a set using the add() method.
numbers = {1, 2, 3}
numbers.add(4)
print("\nAfter adding 4:", numbers)  # Output: {1, 2, 3, 4}

# Update a set with multiple items using the update() method.
numbers.update([5, 6, 7])
print("After updating with [5, 6, 7]:", numbers)  # Output: {1, 2, 3, 4, 5, 6, 7}

# ==================================================
# REMOVING AN ELEMENT FROM A SET
# ==================================================

# Use the discard() method to remove an element.
languages = {"Python", "Java", "C++"}
languages.discard("Java")
print("\nAfter removing 'Java':", languages)  # Output: {'Python', 'C++'}

# ==================================================
# BUILT-IN FUNCTIONS WITH SETS
# ==================================================

# Common built-in functions for sets:
# - len(): Returns the number of elements in a set.
# - max(): Returns the maximum element in a set.
# - min(): Returns the minimum element in a set.
# - sum(): Returns the sum of all elements in a set.
# - sorted(): Returns a sorted list of elements in a set.

print("\nBuilt-in functions with sets:")
print("Length of numbers set:", len(numbers))  # Output: 6
print("Max element in numbers set:", max(numbers))  # Output: 7
print("Min element in numbers set:", min(numbers))  # Output: 1
print("Sum of numbers set:", sum(numbers))  # Output: 28
print("Sorted numbers set:", sorted(numbers))  # Output: [1, 2, 3, 4, 5, 6, 7]

# ==================================================
# ITERATING OVER A SET
# ==================================================

# We can iterate through each element in a set using a loop.
print("\nIterating over a set:")
for fruit in fruits:
    print(fruit)

# ==================================================
# PYTHON SET OPERATIONS
# ==================================================

# Sets support mathematical operations like union, intersection, difference, and symmetric difference.

# Union of Two Sets
A = {1, 2, 3}
B = {3, 4, 5}
print("\nUnion of A and B (A | B):", A | B)  # Output: {1, 2, 3, 4, 5}
print("Union of A and B (A.union(B)):", A.union(B))  # Output: {1, 2, 3, 4, 5}

# Intersection of Two Sets
print("Intersection of A and B (A & B):", A & B)  # Output: {3}
print("Intersection of A and B (A.intersection(B)):", A.intersection(B))  # Output: {3}

# Difference of Two Sets
print("Difference of A and B (A - B):", A - B)  # Output: {1, 2}
print("Difference of A and B (A.difference(B)):", A.difference(B))  # Output: {1, 2}

# Symmetric Difference of Two Sets
print("Symmetric Difference of A and B (A ^ B):", A ^ B)  # Output: {1, 2, 4, 5}
print("Symmetric Difference of A and B (A.symmetric_difference(B)):", A.symmetric_difference(B))  # Output: {1, 2, 4, 5}

# ==================================================
# CHECK IF TWO SETS ARE EQUAL
# ==================================================

# Use the == operator to check if two sets are equal.
C = {1, 2, 3}
D = {3, 2, 1}
print("\nAre sets C and D equal?", C == D)  # Output: True

# ==================================================
# OTHER PYTHON SET METHODS
# ==================================================

# Common set methods:
# - clear(): Removes all elements from the set.
# - copy(): Returns a shallow copy of the set.
# - pop(): Removes and returns an arbitrary element from the set.
# - remove(): Removes a specific element (raises an error if the element is not found).

# Example:
A.clear()
print("\nAfter clearing set A:", A)  # Output: set()

# ==================================================
# MORE RESOURCES
# ==================================================

# For more information, check out:
# - https://www.geeksforgeeks.org/sets-in-python/
# - https://realpython.com/python-sets/

# ==================================================
# END OF SETS DEMO
# ==================================================