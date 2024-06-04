# define the three linked lists.
names = ["Brad", "Tom", "Jane", "Kyle", "Anna"]
companies = ["Goldman Sachs", "HSBC", "JP Morgan", "Deutsche Bank", "Bank of America"]
salaries = [120, 85, 235, 92, 110]

# print out in readable format
for i in range(0, len(names)):
    print(names[i], "works at:", companies[i], "and makes:", salaries[i], "k")

position = 0
# ask user for which to delete
del_who = input("Which one do you want to delete? ")
# loop the name array
for i in range(0, len(names)):
    # compare name
    if names[i] is del_who:
        # save the position
        position = i
        # pop using the position
        names.pop(i)
        companies.pop(i)
        salaries.pop(i)

# re-print the info
for i in range(0, len(names)):
    print(names[i], "works at:", companies[i], "and makes:", salaries[i], "k")
