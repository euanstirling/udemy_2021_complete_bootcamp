
#! FILES
#!

# * This will read a file that is located in the same lacation as your python script or notebook
myfile = open("myfile.txt")

# myfile = open("whoops_wrong.txt")

print(myfile.read())

# * If you have already read the file, you need to return to the start of the file again if you want to read it again
myfile.seek(0)

# * Take the contents of the file and assign to a variable
contents = myfile.read()

print(contents)

myfile.seek(0)

# * Read the file a list
print(myfile.readlines())

#! Open a text file in any locartion

# * Provide the full file path of the file location


#! You need to make sure you also close any file that has been opened or you can get errors

myfile.close()

# * To avoid having to close the file, you can us the "with" method to assign a new variable (in the example below, the new variable is after the "as" and is called my_new_file )

with open("myfile.txt") as my_new_file:
    contents = my_new_file.read()

print(contents)

# * WITH FUNCITON MODES
# * mode="r" is read only
# * mode="w" is write only
# * mode="a" is append only (will add on to files)
# * mode="r+" is reading and writing
# * mode="w+" is writing and reading (overwrites existing files or creates a new file!)

# * To read a file
# with open("my_new_file.txt", mode="r") as f:
#     print(f.read())

# * To append a file (remember to add a new line in added text)
with open("my_new_file.txt", mode="a") as f:
    f.write("\neven more text")

with open("my_new_file.txt", mode="r") as f:
    print(f.read())

# * write mode (it will overwrite an existing or create a new file)
with open("aother_text_file.txt", mode="w") as g:
    g.write("I created this file")

with open("aother_text_file.txt", mode="r") as g:
    print(g.read())
