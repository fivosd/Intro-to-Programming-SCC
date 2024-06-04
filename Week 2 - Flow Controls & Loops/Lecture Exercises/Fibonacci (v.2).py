# Program to display the Fibonacci sequence up to n-th term
nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
n3 = 0
count = 0

# check if the number of terms is valid
if nterms <= 0:
    print("Error. Please enter a positive integer")
# If it is 1 then just output n1 since n1 is the first term.
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
# If it is larger than 1 then calculate.
else:
    # User interaction statement.
    print("Fibonacci sequence:")
    # While loop to ensure that it runs up to nterms
    for i in range(0, nterms):
        # Print the term before we add
        print(n1)
        # add
        n3 = n1 + n2
        # update values
        n1 = n2
        n2 = n3
        # update the count (i.e., iteration counter)
        count = count + 1
