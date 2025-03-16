# Creating a Set
my_set: set = {123, 452, 5, 6}
my_set2: set = set([123, 452, 5, 6])
print("my_set:", my_set)
print("my_set2:", my_set2)
print("Type of my_set:", type(my_set))
print("Type of my_set2:", type(my_set2))
print("Are both sets equal?", my_set == my_set2)


# Holds only Immutable Objects
# Attempting to add a list to a set (This will raise a TypeError)
# my_set = {[123, 452, 5, 6]}

multi_type_set: set = {7, 9.0, False, True, "Hello! World", (1, 5, 9, 'hi')}
print("Set with multiple data types:", multi_type_set)


# Set is Unordered


set2: set = {'Java', 'Python', 'JavaScript', 'java'}
print("Unordered Set:", set2)


# Set is Unchangeable
my_set: set = {1, 2, 3, 4, 5}

try:
    my_set[0] = 10  
except TypeError as e:
    print("Error:", e)

# Adding and Removing Elements


my_set.add(6)
print("Set after adding an element:", my_set)

my_set.remove(3)
print("Set after removing an element:", my_set)

my_set.discard(10)  
print("Set after discard operation:", my_set)

# Removing Multiple Elements


my_set.difference_update({1, 5, 'A'})  
print("Set after removing multiple elements:", my_set)

# Union of Sets


set1: set = {1, 2, 3, 5}
set2: set = {1, 5, 6, 7}
union_set = set1.union(set2)
print("Union using union() method:", union_set)

union_set_operator = set1 | set2
print("Union using '|' operator:", union_set_operator)


# Unique Elements in Set


unique_set: set = {1, 2, 3, 4, 5, "Hello! World"}
unique_set.add(2) 
unique_set.add("Hello! World") 
print("Set after attempting to add duplicates:", unique_set)


# Difference Between remove() and discard()


sample_set: set = {1, 2, 3}

# This will raise an error as 4 is not in the set
# sample_set.remove(4)

# This will not raise an error even if the element does not exist
sample_set.discard(4)


# Pop Method in Set
pop_set = {1, 2, 3}
pop_set.pop()  # Removes an arbitrary element
print("Set after pop operation:", pop_set)
