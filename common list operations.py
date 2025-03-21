#Common List Operations
#Add Elements

#append(): Adds an element to the end of the list.

#insert(): Inserts an element at a specific index.

#extend(): Adds multiple elements (from another list) to the end.


fruits = ["apple", "banana"]
fruits.append("cherry")  # Adds 'cherry' to the end
fruits.insert(1, "orange")  # Inserts 'orange' at index 1
fruits.extend(["grape", "mango"])  # Adds multiple elements
print(fruits)  # Output: ['apple', 'orange', 'banana', 'cherry', 'grape', 'mango']



#Remove Elements

#remove(): Removes the first occurrence of a value.

#pop(): Removes and returns the element at a specific index (default is the last element).

#del: Deletes an element or slice.

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")  # Removes 'banana'
fruits.pop(1)  # Removes and returns the element at index 1
del fruits[0]  # Deletes the first element
print(fruits)  # Output: []



#Check if an Item Exists
#Use the in keyword to check if an item is in the list.


fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Output: True
print("grape" in fruits)   # Output: False


#List Length
#Use the len() function to get the number of items in the list.


fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Output: 3



#Sorting
#sort(): Sorts the list in place (ascending by default).
#sorted(): Returns a new sorted list without modifying the original.

numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()  # Sorts the list in place
print(numbers)  # Output: [1, 1, 3, 4, 5, 9]

sorted_numbers = sorted(numbers, reverse=True)  # Returns a new sorted list in descending order
print(sorted_numbers)  # Output: [9, 5, 4, 3, 1, 1]



#slicing
#You can extract a portion of the list using slicing.
fruits = ["apple", "banana", "cherry", "orange", "mango"]
print(fruits[1:4])  # Output: ['banana', 'cherry', 'orange']
print(fruits[:3])   # Output: ['apple', 'banana', 'cherry']
print(fruits[2:])   # Output: ['cherry', 'orange', 'mango']


#Nested Lists
#Lists can contain other lists, creating a nested structure.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # Output: 6 (second row, third column)


#List Comprehension
#List comprehension is a concise way to create lists.

# Create a list of squares
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]




#Key Points to Remember
#Lists are ordered and mutable.

#They can store heterogeneous data types.

#Use indexing ([index]) to access elements and slicing ([start:end]) to extract sublists.

#Common methods: append(), insert(), remove(), pop(), sort(), etc.