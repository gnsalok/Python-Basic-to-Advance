'''


Modes :-
Character   Meaning
'r'     open for reading (default)
'w'     open for writing, truncating the file first
'x'     open for exclusive creation, failing if the file already exists
'a'     open for writing, appending to the end of the file if it exists
'b'     binary mode
't'     text mode (default)
'+'     open a disk file for updating (reading and writing)
'U'     universal newlines mode (deprecated)



File Handling and more...

#Reading the file
with open("test.txt", "r") as f:
    data = f.read()
    print(data)

# write inside the file
with open("test.txt", "w") as f:
    data = "Wrting test inside the file"
    f.write(data)

# append inside the file
with open("test.txt", "a") as f:
    data = "Wrting test inside the file"
    f.writelines(data)


'''

# append inside the file
with open("test.txt", "a") as f:
    data = "Wrting test inside the file"
    f.writelines(data)
