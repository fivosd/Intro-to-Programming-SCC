# Declaring the three boolean states. Smaller than, Larger than, Equal.
a = None
b = None
c = None

# Declaring the two Numbers. This is not a necessary command.
num1 = 0
num2 = 0

# Getting input from the user. Make sure to convert to int.
num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))

# Making the three Boolean comparisons and appending the value to the boolean variables.
a = (num1 > num2)
b = (num1 < num2)
c = (num1 == num2)

# Outputting each state with a "True" or "False" output.
print("Is Number1 larger than Number2: ")
print(a)

print("Is Number1 smaller than Number2: ")
print(b)

print("Are the numbers equal: ")
print(c)
