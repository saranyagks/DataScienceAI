# print 0 to 20 in the listclear
list1 = list(range(21))
print(list1)

# print range 10 to 20 in the list
list1 = list(range(10, 21))
print(list1)

# print number of items in the list using len function
list1 = [10, 20, 14, 55, 43, 87, 76]
print(len(list1))

# print the each letter in word for an the each iteration
word = "Artificial Intelligence"
for letter in word:
    print(letter)

# print mixed data type using tuples
tup = (1, "Welcome", 2, "Hope", 3, "You", 4, "Enjoy", 5, "Learning")  # tuple
print(tup)

# print nested tuple
tup1 = (0, 1, 2, 3)
tup2 = ("python", "Hope")
tup3 = (tup1, tup2)
print(tup3)

# print Odd numbers in the list
list1 = [20, 10, 16, 19, 25, 1, 276, 188]
for num in list1:
    if num % 2 != 0:
        print(num, end=" is Odd Numner\n")

# print Even numbers in the list
list1 = [20, 10, 16, 19, 25, 1, 276, 188]
for num in list1:
    if num % 2 == 0:
        print(num, end=" is Even Numner\n")
