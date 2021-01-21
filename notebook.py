# Notebook

filename = "notebook.txt"
try:
    file = open(filename, "r")
    file.close()
except IOError:
    print("Could not find a notebook to open, so I created one for you.")
    file = open(filename, "w")
    file.close()
while True:
    print("---",filename,"---")
    print("1 - Add a note")
    print("2 - Read the notes")
    print("3 - Change/Create a notebook")
    print("4 - Erase the notebook")
    print("5 - Quit\n")
    selection = input("Please select one of the above:")
    if selection.isdigit():
        selection = int(selection)
    else:
        print("Please select a number (1-4)!")
        continue
    if selection == 1:
        file = open(filename, "a")
        content = input("Write a new note:")
        file.write(content + "\n")
        file.close()
        print()
    elif selection == 2:
        file = open(filename, "r")
        content = file.readlines()
        for i in content:
            print(i[:-1])
        file.close()
        print()
    elif selection == 3:
        print("Search for a file, if it can't be found, I will create one.")
        name = input("Type the name of the file (*.txt):")
        try:
            file = open(name, "r")
            file.close()
        except IOError:
            print("No file with that name was found, I will create one for you.")
            file = open(name, "w")
            file.close()
        filename = name
        print()
    elif selection == 4:
        while True:
            print("All contents of this notebook will be deleted!")
            prompt = input("Are you sure you want to delete everything, Y/N?")
            if prompt == "N":
                print()
                break
            elif prompt == "Y":
                file = open(filename, "w")
                file.close()
                print("All notes were deleted.")
                print()
                break
    elif selection == 5:
        print("Exiting the notebook, goodbye.")
        break
    else:
        print("Incorrect selection")