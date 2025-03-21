#Task 3: Person Information Dictionary
#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.


# Task 3: Person Information Dictionary

# Step 1: Create an empty dictionary
person = {}

# Step 2: Ask the user for input and store it in the dictionary
person["name"] = input("Enter your name: ")
person["age"] = int(input("Enter your age: "))
person["favorite_color"] = input("Enter your favorite color: ")

# Step 3: Print the dictionary
print("\nPerson Information:")
for key, value in person.items():
    print(f"{key.capitalize()}: {value}")
