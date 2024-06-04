# opens the file
file = open("/Input text blurbs/text2.txt", "r")
# reads -> i.e., converts the file object to string
main = file.read()
# replaces any new lines (\n) with blanks
main = main.replace("\n", " ")
# replaces commas and fullstops with blanks
main = main.replace(".", "")
main = main.replace(",", "")
# splits at blanks
list_of_words = main.split(" ")

