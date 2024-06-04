# Define the array
list = [1, 2, 3, 4, 5, '6', '7', 8, 9, 10]
# Use for loop with IN iteration - it will iterate for the items in list, selecting them one-by-one
for i in list:
    # type check with IS NOT
    if type(i) is not int:
        # use of remove
        list.remove(i)

# print to be used in Debugging
for i in list:
    print(i)
