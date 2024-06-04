# these are the operators the application supports
operators = ['+', '-', '/', '*', '%', '^']
# user input
st = input("What do you want to calculate?\n")
# placeholder char variable for the operator the input has
current = ''
# loops through the array
for op in operators:
    # checks to see if the operator exists in the input
    if op in st:
        # splits, saves the operator and breaks
        st = st.split(op)
        current = op
        break

# saves our operands and creates the result var
piece1 = float(st[0])
piece2 = float(st[1])
result = 0.0

# massive 'switch' type statement
if current is '+':
    result = piece1 + piece2
elif current is '-':
    result = piece1 - piece2
elif current is '/':
    # zero catch since we can't have division with zero
    if piece2 != 0:
        result = piece1/piece2
    else:
        print("Error, you tried to divide with 0!")
elif current is '*':
    result = piece1*piece2
elif current is '%':
    result = piece1 % piece2
elif current is '^':
    result = piece1**piece2

# print and end
print(result)
