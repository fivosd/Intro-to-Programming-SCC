# Define the arrays
names = ["mike", "tony", "greg", "shaq", "elias", "john"]
times = [10.2, 11.3, 11.7, 10.1, 14.5, 13.2, 12.1]

# loop with numbers (range())
for i in range(0, len(names)):
    # check to see if they match
    if names[i] is "john":
        # remove() since we know the name
        names.remove("john")
        # use pop() with the index and print pop() since it returns the value
        print(times.pop(i))
