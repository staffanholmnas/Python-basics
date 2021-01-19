# Notebook
filename = "notebook.txt"
while True:
    print("1 - Add a note")
    print("2 - Read the notes")
    print("3 - Erase the notebook")
    print("4 - Quit\n")
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
    elif selection == 2:
        file = open(filename, "r")
        content = file.readlines()
        for i in content:
            print(i[:-1])
        file.close()
        print()
    elif selection == 3:
        while True:
            prompt = input("Are you sure you want to delete the notebook, Y/N?")
            if prompt == "N":
                break
            elif prompt == "Y":
                file = open(filename, "w")
                file.close()
                print("All notes were deleted.")
                break
    elif selection == 4:
        print("Exiting the notebook, goodbye.")
        break
    else:
        print("Incorrect selection")