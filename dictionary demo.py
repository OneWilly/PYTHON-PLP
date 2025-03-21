# ==================================================
# PYTHON DICTIONARIES
# ==================================================

# A dictionary is an ordered collection (starting from Python 3.7) of items.
# It stores elements in key/value pairs, where keys are unique identifiers
# associated with each value.

# ==================================================
# CREATING A DICTIONARY
# ==================================================

# Example: Storing countries and their capitals
capital_city = {
    "Nepal": "Kathmandu",
    "Italy": "Rome",
    "England": "London"
}
print("Dictionary of countries and capitals:", capital_city)

# Keys are "Nepal", "Italy", "England"
# Values are "Kathmandu", "Rome", "London"

# Note: Keys and values can be of different data types.

# Example 1: Dictionary with mixed data types
numbers = {
    1: "One",
    2: "Two",
    3: "Three"
}
print("\nDictionary with mixed data types:", numbers)

# ==================================================
# ADDING ELEMENTS TO A DICTIONARY
# ==================================================

# We can add elements to a dictionary using the dictionary name with [].
capital_city["Japan"] = "Tokyo"
print("\nAfter adding Japan:", capital_city)

# ==================================================
# CHANGING THE VALUE OF A DICTIONARY
# ==================================================

# We can change the value associated with a key using [].
student_id = {
    111: "Kyle",
    112: "Eric",
    113: "Butters"
}
print("\nOriginal student_id dictionary:", student_id)

# Change the value associated with key 112
student_id[112] = "Stan"
print("After changing value for key 112:", student_id)

# ==================================================
# ACCESSING ELEMENTS FROM A DICTIONARY
# ==================================================

# We use keys to access their corresponding values.
print("\nAccessing dictionary elements:")
print("Capital of Nepal:", capital_city["Nepal"])
print("Student with ID 113:", student_id[113])

# Trying to access a non-existent key will raise an error.
# Uncomment the line below to see the error.
# print(capital_city["USA"])  # KeyError: 'USA'

# ==================================================
# REMOVING ELEMENTS FROM A DICTIONARY
# ==================================================

# We use the `del` statement to remove an element from the dictionary.
del student_id[111]
print("\nAfter removing key 111:", student_id)

# We can also delete the entire dictionary.
del student_id
# Uncomment the line below to see the error.
# print(student_id)  # NameError: name 'student_id' is not defined

# ==================================================
# DICTIONARY METHODS
# ==================================================

# Common dictionary methods:
# - keys(): Returns all keys
# - values(): Returns all values
# - items(): Returns all key-value pairs
# - get(): Returns the value for a key (avoids KeyError)
# - pop(): Removes and returns the value for a key
# - update(): Adds or updates key-value pairs

# Example:
print("\nDictionary methods:")
print("Keys in capital_city:", capital_city.keys())
print("Values in capital_city:", capital_city.values())
print("Key-value pairs in capital_city:", capital_city.items())

# Using get() to avoid KeyError
print("Capital of USA:", capital_city.get("USA", "Not found"))

# Using pop() to remove a key-value pair
removed_value = capital_city.pop("Italy")
print("Removed value for key 'Italy':", removed_value)
print("After popping 'Italy':", capital_city)

# Using update() to add/update key-value pairs
capital_city.update({"France": "Paris", "Germany": "Berlin"})
print("After updating with new countries:", capital_city)

# ==================================================
# DICTIONARY MEMBERSHIP TEST
# ==================================================

# We can test if a key is in a dictionary using the `in` keyword.
# Note: Membership test is only for keys, not values.
print("\nMembership test:")
print("Is 'Nepal' in capital_city?", "Nepal" in capital_city)  # Output: True
print("Is 'Paris' in capital_city?", "Paris" in capital_city)  # Output: False

# ==================================================
# ITERATING THROUGH A DICTIONARY
# ==================================================

# We can iterate through each key in a dictionary using a loop.
print("\nIterating through a dictionary:")
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
for key in squares:
    print(f"Key: {key}, Value: {squares[key]}")

# Alternatively, use items() to iterate through key-value pairs.
print("\nIterating using items():")
for key, value in squares.items():
    print(f"Key: {key}, Value: {value}")

# ==================================================
# MORE RESOURCES
# ==================================================

# For more information, check out:
# - https://www.w3schools.com/python/python_dictionaries.asp
# - https://realpython.com/python-dicts/

# ==================================================
# END OF DICTIONARY DEMO
# ==================================================