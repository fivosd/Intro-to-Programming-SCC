# input string
str = "we have archived big brain"
# the encryption key & modulo of the key
key = 10
key = key % 26
# converts to lowercase !! important
str.lower()
# makes a list of the characters
main_list = list(str)
# loops the list
for i in range(0, len(main_list)):
    # checks to not change the spaces
    if main_list[i] != " ":
        # performs the encryption
        main_list[i] = chr((ord(main_list[i]) + key - 97) % 26 + 97)

# placeholder
out = ""
# join function puts the list (of letters) back together
out = out.join(main_list)
print(out)
