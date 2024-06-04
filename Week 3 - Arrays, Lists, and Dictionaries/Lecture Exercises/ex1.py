# defining the mylist
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# run the input
inp = int(input("What are you looking for in the array? "))

# use type check to ensure that the input type and array type are the same
if type(inp) is type(mylist[0]):
    # Linear search code
    for i in range(0, len(mylist)):
        if mylist[i] == inp:
            print("element found")
            break
# if they don't match
else:
    print("The data types do not match")

# the logic error here is that for example in this code,
# because the input is an integer conversion, if we input anything but
# an int the program will just break at Line 4
