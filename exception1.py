try:
    file = open("testfile.txt", "w")
    file.write("I can write this")
except IOError:
    print("Error: No you fool. File doesn't exist")
else:
    print("There you go my good sir")
