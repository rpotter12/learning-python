myfile=open('text.txt')
print(myfile.read()) # reads all the data of the file

# after running .read() command for one time the cursor reached to the end of the file
# if you try to read the file again
print(myfile.read()) # the output will be empty 

# to take the cursor at the beginning use .seek(0)
myfile.seek(0)
print(myfile.read()) # now the it will print all the data and the cursor again comes to the end

myfile.seek(0)

# to print each line in same line, use .readlines()
print(myfile.readlines())

# to close the file use .close()
myfile.close()

