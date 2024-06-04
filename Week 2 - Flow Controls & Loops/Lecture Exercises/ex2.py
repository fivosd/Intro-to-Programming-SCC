# Define the only variable we need
main_sum = 0

# Run the loop between 0 and 100. Remember 'i' will take a value less than the right side value in Range.
for i in range(0, 101):
    # This is the "smart" version of: main_sum = main_sum + i.
    main_sum += i

# Print to the user.
print(main_sum)
