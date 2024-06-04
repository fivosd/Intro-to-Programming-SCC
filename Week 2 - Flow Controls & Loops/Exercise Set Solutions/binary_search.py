# Define the array.
array1 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
# Define the "moving bounds". Bottom is 0 and top is the length of the array. Mid is calculated later.
bottom = 0
top = len(array1)
mid = 0
# Two flags. One to optimize the search and one for the output switch.
flag = False
found = False
# Two indicator indexes. One for the not found exit. One to give us the position of the element.
position = 0


# THIS IS CODE ETIQUETTE YOU DON'T NEED TO HAVE THIS LINE. This is done so we can use non sorted arrays as input.
array1.sort()

# This gets user input in the form of an integer.
query = int(input("Please enter the number you are looking for: "))

# This loop runs while this flag is false.
while not flag:
    # Loop the array up until it is out of elements
    for i in range(0, len(array1)):
        # Calculate the mid point
        mid = round(((top + bottom)//2))

        # If the query is smaller than the max of the array is the med. I.e., it looks at the lower half of the array.
        if query < array1[mid]:
            top = mid
        # If the query is larger than it looks at the upper half of the array.
        elif query > array1[mid]:
            bottom = mid
        # If the query is equal to the mid then: Save the position, change the flag and, mark it as found.
        # The loop should stop here.
        elif query == array1[mid]:
            position = mid
            flag = True
            found = True
            # Break to exit the for loop.
            break
        # If we reach the limit, then change the flag as true, so we can exit the while loop.
        if i == len(array1):
            flag = True


# Print given if the query is found or not.
if found:
    print("The element was found at: ", mid)
else:
    print("The element was not found.")

# NOTE this is optimized code. It is designed to run as few times as possible. This means that for example,
# if we are looking for the element in the middle of the array, there will only be one numeric comparison. This
# program runs up until we find the element when it kills the loop and outputs to the user. Other implementations
# run until the end of the array which can impact performance in larger arrays. I.e., imagine searching through 1,
# 000,000 elements.
