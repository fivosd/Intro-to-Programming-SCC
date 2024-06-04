# Define an array
array = []
# Prompt user
size = int(input("How many elements can the array hold: "))
a_n = 0

# Fill loop
for i in range(0, size):
    # Calculate a_n using the sequence formula
    a_n = 2 + 2*(i-1)
    # Append
    array.append(a_n)

# Print the array as a whole. This is just for debugging purposes
for i in array:
    print(i)
