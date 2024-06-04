# the list
items = ["Car", "House", "Cat"]

# infinite loop
while 0 < 1:
    # the new item is a String input
    new_item = input("What is the new item you have? ")
    # this kill switch is designed to ensure that the
    # infinite loop can stop.
    if new_item == "Kill":
        break
    # append the item to the list
    items.append(new_item)
    # print list length
    print("You now have:", len(items), "Items")
