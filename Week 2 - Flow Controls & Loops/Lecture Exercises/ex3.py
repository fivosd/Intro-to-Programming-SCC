# Defining the array
array1 = [1, 3, 11, 0, 2, 92, 420, 8, 34, 69]

# Defining the query variable
query = 0
# Asking for user input
query = int(input("What int value are you looking for?: "))
# Defining our flag
flag = False

for i in range(0,10):
    if query == array1[i]:
        flag = True
        break

if flag == True:
    print("The value exists")
else:
    print("The value doesn't exist")
