# the regex library
import re
# opens the file and converts to string
file = open("btb.txt", "r")
main = file.read()
# splits at '@' and '\n'
main = re.split('[@\n]', main)
# we know by investigation which cell contains what, so we just move them into variables
writer = main[1]
media = main[3]
# print
print(writer, media)
