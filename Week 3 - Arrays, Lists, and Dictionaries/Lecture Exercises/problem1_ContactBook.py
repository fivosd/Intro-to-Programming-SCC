# The keys array serves as a user readable (printable) list of the fields
keys = ["first name", "surname", "phone", "school"]
# empty arrays to be populated later
contacts = []
person = {}

# infinite loop
while 0 < 1:
    # creating a menu
    print("\n")
    print("Welcome to Dict Contacts 1.0")
    print("1: View Contacts")
    print("2: Add Contacts")
    print("3: Delete Contacts")
    print("4: Shutdown")
    menu_1 = int(input(":"))
    # we can use a Switch here, but I like the IF more

    # VIEW CONTACTS
    if menu_1 is 1:
        # check to ensure that contacts exist
        if len(contacts) != 0:
            print("\n")
            # print an indexed set of first names from 0 to len(contacts)-1
            for i in range(0, len(contacts)):
                # using .get() we output the first name of each
                print(i, ":", contacts[i].get('first name'))
                # prompt the user
                menu_view = int(input("Which contact do you want to view: "))
                print("\n")
                # this function prints out the data in the contact dict
                for i in keys:
                    print(i, ":", contacts[menu_view].get(i))
        # edge case catch if there are no contacts,
        # this is important because we have input for an index at LINE 30
        # if the array is empty that input will crash at any input
        else:
            print("There are no contacts to view.")

    # ADD Functionality
    if menu_1 is 2:
        print("\n")
        # print out each field that is to be inputted
        for i in keys:
            # print out the filed name
            inp = input(i)
            # creates a new filed with Key = i & Entry = inp
            person[i] = inp
        # appends the 'person' dictionary into the array
        contacts.append(person)
        # clears the dictionary so it can be reused
        person = {}

    # DELETE Functionality
    if menu_1 is 3:
        print("\n")
        # show all the contacts with an index
        for i in range(0, len(contacts)):
            print(i, ":", contacts[i].get('first name'))
        # user input
        menu_del = int(input("Which contact do you want to delete: "))
        # use .pop() since we use an index and pop() uses the index
        contacts.pop(menu_del)
        # user I/O
        print("Done.")

    # Kill switch
    if menu_1 is 4:
        break
