# Notebook
filename = "notebook.txt"
while True:
    print("(1) Read the notebook")
    print("(2) Add note")
    print("(3) Empty the notebook")
    print("(4) Quit\n")
    selection = input("Please select one:")
    if selection.isdigit():
        selection = int(selection)
    else:
        print("Not a number")
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
        print("Notes deleted.")
    elif selection == 4:
        print("Notebook shutting down, thank you.")
        break
    else:
        print("Incorrect selection")