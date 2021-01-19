# Notebook
filename = "notebook.txt"
while True:
    print("1 - Read the notebook")
    print("2 - Add a note")
    print("3 - Erase the notebook")
    print("4 - Quit\n")
    selection = input("Please select one of the above:")
    if selection.isdigit():
        selection = int(selection)
    else:
        print("Please select a number (1-4)!")
        continue
    if selection == 1:
        file = open(filename, "r")
        content = file.readlines()
        for i in content:
            print(i[:-1])
        file.close()
        print()
    elif selection == 2:
        file = open(filename, "a")
        content = input("Write a new note:")
        file.write(content + "\n")
        file.close()
    elif selection == 3:
        file = open(filename, "w")
        file.close()
        print("All notes were deleted.")
    elif selection == 4:
        print("Exiting the notebook, good bye.")
        break
    else:
        print("Incorrect selection")