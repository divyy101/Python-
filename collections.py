# List creation: square brackets create a list.
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = [11, 12, 13]

# Concatenation (+): combines the elements of list2 and list3 into a new list.
list2 = list2 + list3
print("List 2 after concatenating list 3:", list2)

# append(): adds one element at the end of a list.
# This loop uses append() to add each element of list2 to list1.
for item in list2:
    list1.append(item)

print("List 1 after appending list 2:", list1)

# Traversal: visit and print every element in list1 using a for loop.
print("Elements in list1:")
for item in list1:
    print(item,end=" ")

# Membership (in): checks whether an element exists in a list.
print("3 is in list1:", 3 in list1)
print("8 is in list2:", 8 in list2)

# remove(): deletes the first matching value from a list.
list1.remove(2)
list2.remove(8)

print("List 1 after removing 2:", list1)
print("List 2 after removing 8:", list2)

# Count odd and even elements while traversing list1.
odd_count = 0
even_count = 0

for item in list1:
    if item % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Odd elements:", odd_count)
print("Even elements:", even_count)

# sum() adds all values, len() returns the number of list elements.
# Divide the sum by the length to calculate the average.
average = sum(list1) / len(list1)
print("Average of list1:", average)

# sort(): arranges the list elements in ascending order.
list1.sort()
print("Sorted list1:", list1)

# del removes an element using its index position.
del list1[0]
print("List1 after removing the element at index 0:", list1)

# pop(): removes and returns an element; without an index it removes the last element.
popped_item = list1.pop()
print("Popped element:", popped_item)
print("List1 after pop():", list1)

# insert(index, value): adds a value at the given index position.
list1.insert(1, 100)
print("List1 after inserting 100 at index 1:", list1)

# clear(): removes every element from a list.
list3.clear()
print("List3 after clear():", list3)

d={"student ":"divy","branch":"IT"}
print(d)
