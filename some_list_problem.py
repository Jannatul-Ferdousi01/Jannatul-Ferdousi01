#some list problem sloution in python

#1sum of list item
l = [1, 2, 3, 4, 5]
s = 0
for i in l:
    s += i
print(s)

#problem 1 in function
l = [1,2,3,4,5,]
def add(a):
    s = 0
    for i in a:
        s += i
    print(s)

add(l)
#problem 1 in loop comprehension
l = [1, 2, 3, 4, 5]

s = sum(i for i in l)

print(s)

#2 multiplies all the items in a list

l = [1,2,5]
s = 1
for i in l:
     s *= i
print(s)
#problem 2 in function
l = [1,2,5]
def mul(b):
    s = 1
    for i in b:
        s *= i
    print(s)
mul(l)
#problem 2 in loop comprehension
from math import prod

l = [1, 2, 5]

# Using the prod function to multiply all elements in the list
s = prod(i for i in l)

print(s)

#3 largest number from a list
li = [1, 9, 10, 0]

# Initialize maax with the first element of the list
maax = li[0]

# Iterate through the list to find the maximum value
for i in li:
    if i > maax:
        maax = i

# Print the maximum value
print(maax)

# problem 3 in function
li = [ 1,9,10,0]
def mxax(li):
    maax = li[0]
    for i in li:
        if maax>i:
            maax = maax
        else:
            maax = i
    return maax
print(mxax(li))

#problem 3 in loop comprehension
li = [1, 9, 10, 0]
maax = max(i for i in li)
print(maax)

#4 smallest number from a list
lo = [11, 9, 2, 0, 5]

# Initialize small with the first element of the list
small = lo[0]

# Iterate through the list to find the smallest value
for a in lo:
    if a < small:
        small = a

# Print the smallest value
print(small)

# problem 4 in function
lo = [ 11,9,2,0,5]
def sm(lo):
    small = lo[0]
    for a in lo:
        if a>small:
            small = small
        else:
            small = a
    return small
print(sm(lo))

#4 in loop comprehension
lo = [11, 9, 2, 0, 5]
small = min(a for a in lo)
print(small)

#5. Write a Python program to count the number of strings where the string lengthis 2 or more and the first and last character are same from a given list of strings.
lis = ["abc", "xyz", "aba", "1221"]
count = 0
for i in lis:
    if len(i)>2 and i[0] == i[-1]:
        count = count+1
        print(i)
count

#problem 5 in function
lis = ["abba", "338", "22122", "effe"]
def con(lis):
    count = 0
    for i in lis:
        if len(i)>2 and i[0] == i[-1]:
            count = count+1
            print(i)
    print(count)
con(lis)

# problem 5 in loop comprehension
lis = ["abc", "xyz", "aba", "1221"]
count = sum(1 for i in lis if len(i) > 2 and i[0] == i[-1])
# Print the matching strings
for i in lis:
    if len(i) > 2 and i[0] == i[-1]:
        print(i)

# Print the count
print(count)

# 6. Write a Python program to get a list, sorted in increasing order by the lastelement in each tuple from a given list of non-empty tuples.
a = [(2,5), (1,2), (4,4), (2,3),(2,1)]
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i][1] > a[j][1]:
            a[j],a[i] = a[i],a[j]
print(a)
# list according (1)
#problem6 in function
a = [(2,5),(1,2),(4,4),(2,3),(2,1)]
def ac1(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i][1]>a[j][1]:
                a[j],a[i] = a[i],a[j]
    return a
ac1(a)

# problem 6 in loop comprehension
a = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
a = sorted(a, key=lambda x: x[1])
print(a)

#7. Write a Python program to remove duplicates from a list.
li = [ 12,133,100,12,100]
l = []
for i in li:
    if i not in l:
        l.append(i)
print(l)

#problem7 in function
lo = [100,122,300,300]
def du(lo):
    l = []
    for i in lo:
        if i not in l:
            l.append(i)
    return(l)
du(lo)

# problem 7 in loop comprehension
li = [12, 133, 100, 12, 100]

# Using a list comprehension to remove duplicates while maintaining order
l = []
[l.append(i) for i in li if i not in l]

print(l)

#8. Write a Python program to check a list is empty or not.
l = []
if len(l)<1:
    print("empty")
else:
    print("not")
print(len(l))

#problem 8 in function
l = []
def em(l):
    if len(l)<1:
        print("empty")
    else:
        print("not")
em(l)

# problem 8 in loop comprehension
l = []

# Using a conditional expression to determine the message
message = "empty" if len(l) < 1 else "not"
print(message)
print(len(l))

#9. Write a Python program to clone or copy a list.
original_list = [ 1,2,3,4]
new_list = list(original_list)
print(original_list)
print(new_list)

#problem 9 in function
ol = [ 11,12,13,10]
def cop(ol):
    nl = list(ol)
    print(ol)
    print(nl)
cop(ol)
# problem 9 in list comprehension
original_list = [1, 2, 3, 4]
new_list = [item for item in original_list]

print(original_list)
print(new_list)

#10. Write a Python program to find the list of words that are longer than n from agiven list of words.
l = ('The quick brown fox jump over the lazy dog')
n = 3
count = 0
for i in l.split():
    if len(i)> n:
        count = count+1
        print(i)
count

#problem 10 in function
l = ('the quick brown fox jumps over the lazy dog')
def lon(l):
    n = 3
    count = 0
    for i in l.split():
        if len(i)>n:
            count = count+1
            print(i)
            print(count)
lon(l)

# problem 10 in loop comprehension
l = 'The quick brown fox jumps over the lazy dog'
n = 3

# Using list comprehension to filter words longer than n
long_words = [i for i in l.split() if len(i) > n]

# Print the long words
for word in long_words:
    print(word)

# Count of long words
count = len(long_words)
print("Count of words longer than", n, ":", count)

#problem11
n= [ 1,2,3,4,5]
x = [5,6,7,8,9]
for i in n:
    for j in x:
        if i == j:
            print("true")
        else:
            print("false")
#problem11 in function
n= [1,2,3,4,5]
x = [5,6,7,8,9]
def comm(n,x):
    for i in n:
        for j in x:
            if i == j:
                print("true")
            else:
                print("false")
comm(n,x)
# problem 11 in loop comprehension
n = [1, 2, 3, 4, 5]
x = [5, 6, 7, 8, 9]

# Using list comprehension to check for matches
results = ["true" if i in x else "false" for i in n]

# Print the results
for result in results:
    print(result)

#problem12
a = ['Red', 'Green', 'white', 'Black', 'pink', 'yellow']
b = []
for i in a:
   if i == a[0] or i == a[4] or i == a [5] :
       continue
   else:
       b.append(i)

print(b)
#problem 12 in function

a = ['rose', 'orange', 'banana', 'jesmin', 'apple']
def remo(a):
    b = []
    for i in a:
        if i == a[1] or i ==a[2] or i == a[4]:
            continue
        else:
            b.append(i)
    return b

remo(a)
# problem 12 in loop comprehension
a = ['Red', 'Green', 'white', 'Black', 'pink', 'yellow']
b = [i for i in a if i not in (a[0], a[4], a[5])]

print(b)

#problem14
a = [1,2,3,4,5,6,7,8,9]
m = []
for i in a:
    if i%2==0:    #even number
        continue
    else:
        m.append(i)
print(m)        
#problem 14 in function
a = [11, 12,13,14,15,16,17,18,19]
def even(a):
    m = []
    for i in a:
        if i%2==0:
            continue       #even number
        else:
            m.append(i)
    return m
even(a)
# problem 14 in loop loop comprehension
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
m = [i for i in a if i % 2 != 0]  # Keep only odd numbers

print(m)
#problem17
n = 30
m = []
for i in range(1, n+1):
    m.append(i**2)
print(m[-5:])

#problem17 in function
n = 30
def sque(n):  
    m = []
    for i in range(1, n+1): 
        m.append(i**2)  
    return m
print(sque(n)[-5:-1]) 

def squ(n):
    m = []
    for i in range(1, n+1):
        m.append(i**2)
    return m 
n =30
print(squ(30)[-6:])

# problem 17 in loop comprehension
n = 30
m = [i**2 for i in range(1, n + 1)]

print(m[-5:])

#18 generate permutations of list
import itertools

print(list(itertools.permutations([1,2,3])))

# 19 get difference between the two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
difference = [item for item in list1 if item not in list2]

print(difference)
# 19 in function
def list_difference(list1, list2):
    difference = [item for item in list1 if item not in list2]
    return difference
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

result = list_difference(list1, list2)
print(result)

# 19 in loop comprehension
def list_difference(list1, list2):
    difference = []
    for item in list1:
        if item not in list2:
            difference.append(item) 
            
    return difference
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

result = list_difference(list1, list2)
print(result)

# 20 access the index of a list
my_list = ['a', 'b', 'c', 'd', 'e']
for index in range(len(my_list)):
    value = my_list[index]
    print(f'Index: {index}, Value: {value}')
# 20 in function
my_list = ['a', 'b', 'c', 'd', 'e']

for index, value in enumerate(my_list):
    print(f'Index: {index}, Value: {value}')
# 20 loop comprehension
my_list = ['a', 'b', 'c', 'd', 'e']

for formatted_string in (f'Index: {index}, Value: {value}' for index, value in enumerate(my_list)):
    print(formatted_string)
# 21 convert a list of character into a string
char_list = ['H', 'e', 'l', 'l', 'o']

# Initialize an empty string
result_string = ''

# Use a for loop to concatenate each character
for char in char_list:
    result_string += char  # Append each character to the result string

print(result_string)
#21 in function
def list_to_string(char_list):
    result_string = ''
    for char in char_list:
        result_string += char 
    
    return result_string
char_list = ['H', 'e', 'l', 'l', 'o']
result = list_to_string(char_list)
print(result)

# 21 in comprehension
def list_to_string(char_list):

    return ''.join(char for char in char_list)
char_list = ['H', 'e', 'l', 'l', 'o']
result = list_to_string(char_list)
print(result)
# 22 find index of an item in a specified list
# Example list
my_list = [10, 20, 30, 40, 50]
item_to_find = 30
index = -1  # Initialize index to -1 (not found)

# Loop through the list to find the index
for i in range(len(my_list)):
    if my_list[i] == item_to_find:
        index = i  # Update index if item is found
        break  # Exit the loop once the item is found

# Check the result
if index != -1:
    print(f"Item {item_to_find} found at index: {index}")
else:
    print(f"Item {item_to_find} not found in the list.")

#22 in function 
def find_index(item, my_list):
    for index in range(len(my_list)):
        if my_list[index] == item:
            return index
    return -1  # Return -1 if the item is not found

# Example usage
my_list = [10, 20, 30, 40, 50]
item_to_find = 30
index = find_index(item_to_find, my_list)

if index != -1:
    print(f"Item {item_to_find} found at index: {index}")
else:
    print(f"Item {item_to_find} not found in the list.")

#22 in loop comprehension
# Example list
my_list = [10, 20, 30, 40, 50]
item_to_find = 30

# Using list comprehension with next() to find the index
index = next((i for i, value in enumerate(my_list) if value == item_to_find), -1)

# Check the result
if index != -1:
    print(f"Item {item_to_find} found at index: {index}")
else:
    print(f"Item {item_to_find} not found in the list.")

#23. Write a Python program to flatten a shallow list.
# Sample shallow list
shallow_list = [[1, 2, 3], [4, 5], [6, 7, 8]]

# Flattening the shallow list
flattened_list = [item for sublist in shallow_list for item in sublist]

# Printing the result
print(flattened_list)
#23 in function
# Function to flatten a shallow list
def flatten_list(shallow_list):
    return [item for sublist in shallow_list for item in sublist]

# Sample shallow list
shallow_list = [[1, 2, 3], [4, 5], [6, 7, 8]]

# Flattening the shallow list using the function
flattened_list = flatten_list(shallow_list)

# Printing the result
print(flattened_list)

#24. Write a Python program to append a list to the second list.
# First list
list1 = [1, 2, 3]

# Second list
list2 = [4, 5, 6]

# Method 1: Using extend()
list2.extend(list1)

# Printing the result after using extend
print("After using extend():", list2)

# Resetting list2 for the next method
list2 = [4, 5, 6]

# Method 2: Using += operator
list2 += list1

# Printing the result after using +=
print("After using += operator:", list2)
#24 in function
# Function to append one list to another using extend
def append_using_extend(list1, list2):
    list2.extend(list1)
    return list2

# Function to append one list to another using += operator
def append_using_plus_equals(list1, list2):
    list2 += list1
    return list2

# First list
list1 = [1, 2, 3]

# Second list
list2 = [4, 5, 6]

# Using the extend method
result_extend = append_using_extend(list1, list2.copy())  # Using copy to avoid modifying the original list2
print("After using extend():", result_extend)

# Using the += operator
result_plus_equals = append_using_plus_equals(list1, list2.copy())  # Using copy to avoid modifying the original list2
print("After using += operator:", result_plus_equals)

#24 in comprehension
# Function to append one list to another using list comprehension
def append_using_comprehension(list1, list2):
    return [item for item in list2] + [item for item in list1]

# First list
list1 = [1, 2, 3]

# Second list
list2 = [4, 5, 6]

# Using the list comprehension method
result_comprehension = append_using_comprehension(list1, list2)

# Printing the result
print("After using list comprehension:", result_comprehension)

#25. Write a Python program to select an item randomly from a list.
import random

# Sample list
items = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Selecting a random item from the list
random_item = random.choice(items)

# Printing the selected random item
print("Randomly selected item:", random_item)

#27. Write a Python program to find the second smallest number in a list.
# Sample list
numbers = [5, 3, 8, 1, 2, 7, 3, 4]

# Removing duplicates by converting the list to a set and then back to a list
unique_numbers = list(set(numbers))

# Sorting the unique numbers
unique_numbers.sort()

# Finding the second smallest number
if len(unique_numbers) >= 2:
    second_smallest = unique_numbers[1]
    print("The second smallest number is:", second_smallest)
else:
    print("There is no second smallest number.")

#27 in function
def find_second_smallest(numbers):
    # Removing duplicates by converting the list to a set and then back to a list
    unique_numbers = list(set(numbers))
    
    # Sorting the unique numbers
    unique_numbers.sort()
    
    # Finding the second smallest number
    if len(unique_numbers) >= 2:
        return unique_numbers[1]
    else:
        return None  # or you can return a message or raise an exception

# Example usage
numbers = [5, 3, 8, 1, 2, 7, 3, 4]
second_smallest = find_second_smallest(numbers)

if second_smallest is not None:
    print("The second smallest number is:", second_smallest)
else:
    print("There is no second smallest number.")

#27 in loop comprehension
def find_second_smallest(numbers):
    # Using list comprehension to create a sorted list of unique numbers
    unique_numbers = sorted(set(numbers))
    
    # Finding the second smallest number
    return unique_numbers[1] if len(unique_numbers) >= 2 else None

# Example usage
numbers = [5, 3, 8, 1, 2, 7, 3, 4]
second_smallest = find_second_smallest(numbers)

if second_smallest is not None:
    print("The second smallest number is:", second_smallest)
else:
    print("There is no second smallest number.")
#28. Write a Python program to find the second largest number in a list.
# Sample list of numbers
numbers = [10, 20, 4, 45, 99, 99]

# Check if the list has at least two distinct numbers
if len(numbers) < 2:
    print("List must contain at least two distinct numbers.")
else:
    first, second = float('-inf'), float('-inf')
    
    for number in numbers:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
            
    if second == float('-inf'):
        print("There is no second largest number (all numbers may be the same).")
    else:
        print("The second largest number is:", second)

#28 in function
def find_second_largest(numbers):
    if len(numbers) < 2:
        return "List must contain at least two distinct numbers."
    
    first, second = float('-inf'), float('-inf')
    
    for number in numbers:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
            
    if second == float('-inf'):
        return "There is no second largest number (all numbers may be the same)."
    
    return second

# Example usage
numbers = [10, 20, 4, 45, 99, 99]
second_largest = find_second_largest(numbers)
print("The second largest number is:", second_largest)
#28 in comprehension
# Sample list of numbers
numbers = [10, 20, 4, 45, 99, 99]

# Check if the list has at least two distinct numbers
if len(numbers) < 2:
    print("List must contain at least two distinct numbers.")
else:
    # Create a sorted list of unique numbers using set and list comprehension
    unique_numbers = sorted(set(numbers), reverse=True)
    
    if len(unique_numbers) < 2:
        print("There is no second largest number (all numbers may be the same).")
    else:
        print("The second largest number is:", unique_numbers[1])
#29. Write a Python program to get unique values from a list.
# Input list
input_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]

# Initialize an empty list to store unique values
unique_values = []

# Iterate through each item in the input list
for item in input_list:
    # Check if the item is not already in the unique list
    if item not in unique_values:
        # If not, add it to the unique list
        unique_values.append(item)

# Print the list of unique values
print("Unique values:", unique_values)
#29 in function
def get_unique_values(input_list):
    unique_values = []  # Initialize an empty list to store unique values
    for item in input_list:  # Iterate through each item in the input list
        if item not in unique_values:  # Check if the item is not already in the unique list
            unique_values.append(item)  # If not, add it to the unique list
    return unique_values  # Return the list of unique values

# Example usage
input_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
unique_list = get_unique_values(input_list)
print("Unique values:", unique_list)
#29 in comprehension
# Input list
input_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]

# Use a set to track seen items and a list comprehension to get unique values
unique_values = []
seen = set()

# List comprehension with a for loop
unique_values = [item for item in input_list if not (item in seen or seen.add(item))]

# Print the list of unique values
print("Unique values:", unique_values)
#30. Write a Python program to get the frequency of the elements in a list.
from collections import Counter

# Sample list
sample_list = [1, 2, 2, 3, 4, 4, 4, 5]

# Use Counter to count the frequency of each element
frequency = Counter(sample_list)

# Print the frequency
for element, count in frequency.items():
    print(f"Element: {element}, Frequency: {count}")
#30 in function
from collections import Counter

def get_frequency(elements):
    # Use Counter to count the frequency of each element
    frequency = Counter(elements)
    return frequency

# Example usage
if __name__ == "__main__":
    # Sample list
    sample_list = [1, 2, 2, 3, 4, 4, 4, 5]
    
    # Get the frequency of elements
    frequency = get_frequency(sample_list)
    
    # Print the frequency
    for element, count in frequency.items():
        print(f"Element: {element}, Frequency: {count}")
#30 in comprehension
# Sample list
sample_list = [1, 2, 2, 3, 4, 4, 4, 5]

# Create a frequency dictionary using a dictionary comprehension
frequency = {element: sample_list.count(element) for element in set(sample_list)}

# Print the frequency
for element, count in frequency.items():
    print(f"Element: {element}, Frequency: {count}")
#31. Write a Python program to count the number of elements in a list within aspecified range.
# Sample list
sample_list = [1, 5, 8, 12, 15, 20, 25, 30]

# Specify the range
lower_bound = 10
upper_bound = 20

# Initialize a counter
count = 0

# Count elements within the specified range using a loop
for element in sample_list:
    if lower_bound <= element <= upper_bound:
        count += 1

# Print the result
print(f"Number of elements in the range [{lower_bound}, {upper_bound}]: {count}")
#31 in function
def count_elements_in_range(elements, lower_bound, upper_bound):
    # Using a list comprehension to count elements within the specified range
    count = sum(lower_bound <= element <= upper_bound for element in elements)
    return count

# Example usage
if __name__ == "__main__":
    # Sample list
    sample_list = [1, 5, 8, 12, 15, 20, 25, 30]
    
    # Specify the range
    lower_bound = 10
    upper_bound = 20
    
    # Count the number of elements in the specified range
    count = count_elements_in_range(sample_list, lower_bound, upper_bound)
    
    # Print the result
    print(f"Number of elements in the range [{lower_bound}, {upper_bound}]: {count}")
#31 in comprehension
# Sample list
sample_list = [1, 5, 8, 12, 15, 20, 25, 30]

# Specify the range
lower_bound = 10
upper_bound = 20

# Count elements within the specified range using a generator expression
count = sum(1 for element in sample_list if lower_bound <= element <= upper_bound)

# Print the result
print(f"Number of elements in the range [{lower_bound}, {upper_bound}]: {count}")
#32. Write a Python program to check whether a list contains a sublist.
def contains_sublist(main_list, sublist):
    sub_length = len(sublist)
    return any(main_list[i:i + sub_length] == sublist for i in range(len(main_list) - sub_length + 1))

# Example usage
if __name__ == "__main__":
    # Sample lists
    main_list = [1, 2, 3, 4, 5, 6]
    sublist = [3, 4]

    # Check if the main list contains the sublist
    if contains_sublist(main_list, sublist):
        print("The main list contains the sublist.")
    else:
        print("The main list does not contain the sublist.")
#32 in function
def contains_sublist(main_list, sublist):
    # Get the lengths of the main list and the sublist
    main_length = len(main_list)
    sub_length = len(sublist)

    # Iterate through the main list
    for i in range(main_length - sub_length + 1):
        # Check if the sublist matches the slice of the main list
        if main_list[i:i + sub_length] == sublist:
            return True
    return False

# Example usage
if __name__ == "__main__":
    # Sample lists
    main_list = [1, 2, 3, 4, 5, 6]
    sublist = [3, 4]

    # Check if the main list contains the sublist
    if contains_sublist(main_list, sublist):
        print("The main list contains the sublist.")
    else:
        print("The main list does not contain the sublist.")
#33. Write a Python program to generate all sublists of a list.
# Original list
original_list = [1, 2, 3]

# Initialize a list to store all sublists
sublists = []

# Generate all possible sublists
for i in range(len(original_list) + 1):
    for j in range(i):
        sublists.append(original_list[j:i])

# Print all sublists
print("All Sublists:")
for sublist in sublists:
    print(sublist)
#33 in function
def generate_sublists(original_list):
    # Initialize a list to store all sublists
    sublists = []

    # Generate all possible sublists
    for i in range(len(original_list) + 1):
        for j in range(i):
            sublists.append(original_list[j:i])

    return sublists

# Example usage
original_list = [1, 2, 3]
sublists = generate_sublists(original_list)

# Print all sublists
print("All Sublists:")
for sublist in sublists:
    print(sublist)
#33 in loop comprehension
def generate_sublists(original_list):
    # Generate all possible sublists using list comprehension
    sublists = [original_list[j:i] for i in range(len(original_list) + 1) for j in range(i)]
    return sublists

# Example usage
original_list = [1, 2, 3]
sublists = generate_sublists(original_list)

# Print all sublists
print("All Sublists:")
for sublist in sublists:
    print(sublist)
#34. Write a Python program using Sieve of Eratosthenes method for computingprimes upto a specified number.
# Specify the upper limit
n = 30

# Create a boolean array "is_prime[0..n]" and initialize
# all entries as true. A value in is_prime[i] will
# finally be false if i is Not a prime, else true.
is_prime = [True] * (n + 1)
p = 2  # Starting from the first prime number

while (p * p <= n):
    # If is_prime[p] is not changed, then it is a prime
    if is_prime[p]:
        # Updating all multiples of p to not prime
        for i in range(p * p, n + 1, p):
            is_prime[i] = False
    p += 1

# Collecting all prime numbers
primes = [p for p in range(2, n + 1) if is_prime[p]]

# Print the prime numbers
print(f"Prime numbers up to {n}: {primes}")
#34 in function
def sieve_of_eratosthenes(n):
    # Create a boolean array "is_prime[0..n]" and initialize
    # all entries as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * (n + 1)
    p = 2  # Starting from the first prime number

    while (p * p <= n):
        # If is_prime[p] is not changed, then it is a prime
        if is_prime[p]:
            # Updating all multiples of p to not prime
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    # Collecting all prime numbers
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes

# Example usage
number = 30  # Specify the upper limit
prime_numbers = sieve_of_eratosthenes(number)

# Print the prime numbers
print(f"Prime numbers up to {number}: {prime_numbers}")
#34 in loop comprehension
# Specify the upper limit
n = 30

# Create a boolean array "is_prime[0..n]" and initialize
# all entries as true. A value in is_prime[i] will
# finally be false if i is Not a prime, else true.
is_prime = [True] * (n + 1)
p = 2  # Starting from the first prime number

while (p * p <= n):
    # If is_prime[p] is not changed, then it is a prime
    if is_prime[p]:
        # Updating all multiples of p to not prime
        for i in range(p * p, n + 1, p):
            is_prime[i] = False
    p += 1

# Collecting all prime numbers using list comprehension
primes = [i for i in range(2, n + 1) if is_prime[i]]

# Print the prime numbers
print(f"Prime numbers up to {n}: {primes}")

#35. Write a Python program to create a list by concatenating a given list whichrange goes from 1 to n.
# Given list
given_list = [10, 20, 30]

# Specify the upper limit n
n = 5

# Create a list with numbers from 1 to n
range_list = list(range(1, n + 1))

# Concatenate the given list with the range list
concatenated_list = given_list + range_list

# Print the resulting concatenated list
print("Concatenated List:", concatenated_list)
#35 in function
def concatenate_with_range(given_list, n):
    # Create a list with numbers from 1 to n
    range_list = list(range(1, n + 1))
    
    # Concatenate the given list with the range list
    concatenated_list = given_list + range_list
    
    return concatenated_list

# Example usage
given_list = [10, 20, 30]  # Given list
n = 5                       # Specify the upper limit n

# Call the function to get the concatenated list
result = concatenate_with_range(given_list, n)

# Print the resulting concatenated list
print("Concatenated List:", result)
#35 in loop comprehension
def concatenate_with_range(given_list, n):
    # Create a list with numbers from 1 to n using list comprehension
    range_list = [i for i in range(1, n + 1)]
    
    # Concatenate the given list with the range list
    concatenated_list = given_list + range_list
    
    return concatenated_list

# Example usage
given_list = [10, 20, 30]  # Given list
n = 5                       # Specify the upper limit n

# Call the function to get the concatenated list
result = concatenate_with_range(given_list, n)

# Print the resulting concatenated list
print("Concatenated List:", result)
#36. Write a Python program to get variable unique identification number or string.
import uuid

# Generate a unique identification number (UUID)
unique_id = uuid.uuid4()

# Print the unique identification number
print("Unique Identification Number:", unique_id)
#36 in function
import uuid

def generate_unique_id():
    # Generate a unique identification number (UUID)
    return uuid.uuid4()

# Example usage
unique_id = generate_unique_id()

# Print the unique identification number
print("Unique Identification Number:", unique_id)

#37. Write a Python program to find common items from two lists.
# Two lists to find common items
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Initialize an empty list to store common items
common_items = []

# Iterate through the first list
for item in list1:
    # Check if the item is in the second list
    if item in list2:
        common_items.append(item)

# Print the common items
print("Common items:", common_items)
#37 in function
def find_common_items(list1, list2):
    # Initialize an empty list to store common items
    common_items = []

    # Iterate through the first list
    for item in list1:
        # Check if the item is in the second list
        if item in list2:
            common_items.append(item)

    return common_items

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Call the function to find common items
result = find_common_items(list1, list2)

# Print the common items
print("Common items:", result)
#37 in loop comprehension
# Two lists to find common items
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Use list comprehension to find common items
common_items = [item for item in list1 if item in list2]

# Print the common items
print("Common items:", common_items)
#38. Write a Python program to change the position of every n-th value with the(n+1)th in a list.
# List of values
values_list = [10, 20, 30, 40, 50, 60, 70, 80]

# Specify the value of n
n = 2  # Change every 2nd value with the next one

# Iterate through the list with a step of n
for i in range(0, len(values_list) - 1, n):
    # Swap the n-th value with the (n+1)-th value
    values_list[i], values_list[i + 1] = values_list[i + 1], values_list[i]

# Print the modified list
print(values_list)
#38 in function
def swap_nth_with_next(values_list, n):
    # Iterate through the list with a step of n
    for i in range(0, len(values_list) - 1, n):
        # Swap the n-th value with the (n+1)-th value
        values_list[i], values_list[i + 1] = values_list[i + 1], values_list[i]

# Example usage
values_list = [10, 20, 30, 40, 50, 60, 70, 80]
n = 2  # Change every 2nd value with the next one

# Call the function to perform the swap
swap_nth_with_next(values_list, n)

# Print the modified list
print(values_list)
#38 in loop comprehension
# List of values
values_list = [10, 20, 30, 40, 50, 60, 70, 80]
n = 2  # Change every 2nd value with the next one

# Create a new list with swapped values using list comprehension
swapped_list = [
    values_list[i + 1] if (i % n == 0 and i + 1 < len(values_list)) else values_list[i]
    for i in range(len(values_list))
]

# Adjust the swapped values back to their original positions
for i in range(0, len(values_list) - 1, n):
    swapped_list[i], swapped_list[i + 1] = swapped_list[i + 1], swapped_list[i]

# Print the modified list
print(swapped_list)
#39. Write a Python program to convert a list of multiple integers into a single nteger.
# List of integers to be converted
int_list = [1, 23, 456, 7, 89]

# Convert the list of integers to a single integer
# First, convert each integer to a string, then join them, and finally convert back to an integer
single_integer = int(''.join(map(str, int_list)))

# Print the result
print(single_integer)
#39 in function
def convert_list_to_single_integer(int_list):
    # Convert the list of integers to a single integer
    # First, convert each integer to a string, then join them, and finally convert back to an integer
    single_integer = int(''.join(map(str, int_list)))
    return single_integer

# Example usage
int_list = [1, 23, 456, 7, 89]
result = convert_list_to_single_integer(int_list)

# Print the result
print(result)
#39 in loop comprehension
def convert_list_to_single_integer(int_list):
    # Use a list comprehension to convert each integer to a string
    # Then join them and convert back to an integer
    single_integer = int(''.join([str(i) for i in int_list]))
    return single_integer

# Example usage
int_list = [1, 23, 456, 7, 89]
result = convert_list_to_single_integer(int_list)

# Print the result
print(result)

#40. Write a Python program to split a list based on first character of word.
# List of words to be split
words_list = ['apple', 'banana', 'apricot', 'blueberry', 'cherry', 'avocado', 'blackberry']

# Initialize an empty dictionary to hold the split lists
split_dict = {}

# Iterate over each word in the list
for word in words_list:
    # Get the first character of the word
    first_char = word[0].lower()  # Convert to lowercase for case insensitivity

    # If the first character is not in the dictionary, add it with an empty list
    if first_char not in split_dict:
        split_dict[first_char] = []

    # Append the word to the corresponding list in the dictionary
    split_dict[first_char].append(word)

# Print the result
for key, value in split_dict.items():
    print(f"{key}: {value}")
#40 in function
def split_list_by_first_character(words):
    # Initialize an empty dictionary to hold the split lists
    split_dict = {}

    # Iterate over each word in the list
    for word in words:
        # Get the first character of the word
        first_char = word[0].lower()  # Convert to lowercase for case insensitivity

        # If the first character is not in the dictionary, add it with an empty list
        if first_char not in split_dict:
            split_dict[first_char] = []

        # Append the word to the corresponding list in the dictionary
        split_dict[first_char].append(word)

    return split_dict

# Example usage
words_list = ['apple', 'banana', 'apricot', 'blueberry', 'cherry', 'avocado', 'blackberry']
result = split_list_by_first_character(words_list)

# Print the result
for key, value in result.items():
    print(f"{key}: {value}")
#40 in comprehension
# List of words to be split
words_list = ['apple', 'banana', 'apricot', 'blueberry', 'cherry', 'avocado', 'blackberry']

# Create a dictionary using dictionary comprehension
split_dict = {}
for word in words_list:
    first_char = word[0].lower()  # Convert to lowercase for case insensitivity
    split_dict.setdefault(first_char, []).append(word)

# Print the result
for key, value in split_dict.items():
    print(f"{key}: {value}")
