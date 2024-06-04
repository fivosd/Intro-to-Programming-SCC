# define the time array and the placeholder array.
times = [9.6, 11.6, 12.8, 9.9, 9.7, 15.9, 13.1, 10.1, 10.3, 10.2]
worst = []

# sort from largest to smaller.
times.sort()
# reverse (flip) the array.
times.reverse()

# look up the first three elements (i.e., the three worst times)
# and save the values into the "worst" array.
for i in range(0, 3):
    worst.append(times[i])

# iterate through "worst" and print the values
# use the lookup type remove function to remove from times.
for i in worst:
    print(i)
    times.remove(i)
