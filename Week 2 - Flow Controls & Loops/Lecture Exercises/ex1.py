# Declare the floats. Non-necessary code.
a = 0.0
b = 0.0
c = 0.0

# Get user input.
a = float(input("Enter the first Number: "))
b = float(input("Enter the second Number: "))

# Check to make sure that b is NOT 0 and then divide & print.
if b != 0:
    c = a/b
    print(c)

# Print an error if it is equal to zero. Non-necessary code, just better user interaction.
if b == 0:
    print("Error. The denominator is 0")
    