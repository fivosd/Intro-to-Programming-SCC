# list of names
names = ['mike', 'andreas', 'fivos', 'john']
# loop -> each i is a string
for i in names:
    # Use the open command and format the name. 'W' module since it is writting onto the file.
    file = open('{}.txt'.format(i), 'w')
    # This writes the name inside each file. The file handler is 'file'
    file.write("hello {}".format(i))
    # Closes the files and saves it
    file.close()
