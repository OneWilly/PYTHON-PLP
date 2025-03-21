# ==================================================
# PYTHON STRINGS WITH USE CASE SCENARIOS
# ==================================================

# A string is a sequence of characters. For example, "hello" is a string containing
# the characters 'h', 'e', 'l', 'l', and 'o'.

# ==================================================
# CREATING A STRING
# ==================================================

# Use Case: Storing a user's name.
name = "Alice"
print("User's name:", name)

# Use Case: Storing a welcome message.
message = "Welcome to Python Programming!"
print("Welcome message:", message)

# Strings can be created using single or double quotes.
single_quoted = 'This is a single-quoted string.'
double_quoted = "This is a double-quoted string."
print("\nSingle-quoted string:", single_quoted)
print("Double-quoted string:", double_quoted)

# ==================================================
# ACCESSING STRING CHARACTERS
# ==================================================

# Use Case: Extracting the first letter of a username.
username = "alice123"
first_letter = username[0]
print("\nFirst letter of username:", first_letter)

# Negative Indexing: Accessing characters from the end.
last_letter = username[-1]
print("Last letter of username:", last_letter)

# Slicing: Extracting a substring.
substring = username[0:5]  # Extract "alice"
print("Substring of username:", substring)

# ==================================================
# STRINGS ARE IMMUTABLE
# ==================================================

# Use Case: Attempting to change a character in a string (will raise an error).
# Uncomment the line below to see the error.
# username[0] = 'A'  # TypeError: 'str' object does not support item assignment

# Instead, create a new string.
new_username = "A" + username[1:]
print("\nNew username after modification:", new_username)

# ==================================================
# MULTILINE STRINGS
# ==================================================

# Use Case: Storing a multi-line address.
address = """
123 Main Street
Apt 4B
New York, NY 10001
"""
print("\nAddress:")
print(address)

# ==================================================
# STRING OPERATIONS
# ==================================================

# 1. Compare Two Strings
# Use Case: Checking if two usernames are the same.
username1 = "alice123"
username2 = "bob456"
username3 = "alice123"

print("\nAre username1 and username2 the same?", username1 == username2)  # Output: False
print("Are username1 and username3 the same?", username1 == username3)  # Output: True

# 2. Join Two or More Strings
# Use Case: Creating a personalized greeting.
greet = "Hello"
name = "Alice"
greeting = greet + ", " + name + "!"
print("\nGreeting:", greeting)

# 3. Iterate Through a String
# Use Case: Counting the number of vowels in a string.
vowels = "aeiou"
count = 0
for char in name.lower():
    if char in vowels:
        count += 1
print(f"Number of vowels in '{name}':", count)

# 4. String Length
# Use Case: Validating the length of a password.
password = "secure123"
if len(password) >= 8:
    print("\nPassword is valid.")
else:
    print("Password is too short.")

# 5. String Membership Test
# Use Case: Checking if a keyword exists in a sentence.
sentence = "Python is a powerful programming language."
keyword = "powerful"
print(f"\nIs '{keyword}' in the sentence?", keyword in sentence)  # Output: True

# ==================================================
# STRING METHODS
# ==================================================

# Use Case: Converting a string to uppercase.
uppercase_name = name.upper()
print("\nUppercase name:", uppercase_name)

# Use Case: Replacing a word in a sentence.
new_sentence = sentence.replace("powerful", "versatile")
print("Updated sentence:", new_sentence)

# Use Case: Splitting a string into a list of words.
words = sentence.split()
print("Words in the sentence:", words)

# ==================================================
# ESCAPE SEQUENCES
# ==================================================

# Use Case: Including quotes inside a string.
quote = "He said, \"Python is amazing!\""
print("\nString with quotes:", quote)

# Use Case: Adding a newline in a string.
multiline = "Line 1\nLine 2\nLine 3"
print("\nMultiline string:")
print(multiline)

# ==================================================
# STRING FORMATTING (F-STRINGS)
# ==================================================

# Use Case: Creating a personalized message using f-strings.
age = 25
personalized_message = f"{name} is {age} years old."
print("\nPersonalized message:", personalized_message)

# ==================================================
# MORE RESOURCES
# ==================================================

# For more information, check out:
# - https://www.simplilearn.com/tutorials/python-tutorial/python-strings
# - https://www.geeksforgeeks.org/python-string/
# - https://www.tutorialspoint.com/python/python_strings.htm

# ==================================================
# END OF STRINGS DEMO WITH USE CASES
# ==================================================