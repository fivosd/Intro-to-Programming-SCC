# Defining the variables. The array. The flag. A Temporary variable for the swap. A counter for the flag switch.
array1 = [12, 24, 1, 9, 42, 8, 3, 0]
flag = False
temp = 0
counter = 0

# Code runs until the array is sorted
while not flag:
    # Counter is how many "sorted" pairs exist in the array at each run.
    counter = 0
    # For loop loops through the array.
    for i in range(0, len(array1)-1):
        # Checks the pair and swaps.
        if array1[i] > array1[i+1]:
            temp = array1[i]
            array1[i] = array1[i+1]
            array1[i+1] = temp
        # Checks the pair, and if they are sorted, it notes it by adding in the counter.
        else:
            counter = counter + 1
            # Checks to see if the pairs are sorted. We use len(array1)-1 as an indicator because if we used len(
            # array1). We would run into an index error as there is no element at i+1 if i is the last element.
            if counter == len(array1)-1:
                # Switch the flag.
                flag = True

# Print the array.
for j in range(0, len(array1)):
    print(array1[j])
    