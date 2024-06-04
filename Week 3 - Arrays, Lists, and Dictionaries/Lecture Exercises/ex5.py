# define the names since we can't see the Keys.
names = ["john", "anne", "mike", "andrew", "tanya"]

# define the phonebook and fill it in.
# these are all fake phone nums don't call them y'all!
phonebook = {
    "john": 30699900161,
    "anne": 30699907691,
    "mike": 30699909912,
    "andrew": 30699906275,
    "tanya": 30699908444,
}

# print out the names so the user can see
for i in names:
    print(i)
# prompt the user for a name input
query = input("Which phone number are you looking for: ")
# this function converts the string to lowercase.
# we do this to ensure that everything is lowercase and no errors will
# occur.
query.lower()

# check if the name exists
if query in phonebook:
    print(query + ":" + phonebook[query])
else:
    print("The name you entered doesn't exits")
