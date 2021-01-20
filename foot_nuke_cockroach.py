import random
def main():
    wins = 0
    ties = 0
    rounds = 0
    print("Welcome to this game of chance, please write and choose:")
    while True:
        number = random.randint(1,3)
        if number == 1:
            outcome = "Foot"
        elif number == 2:
            outcome = "Nuke"
        elif number == 3:
            outcome = "Cockroach"
        selection = input("Foot, Nuke or Cockroach? Press Q to quit:")
        if selection == outcome:
            ties = countties(ties, selection, outcome)
        elif selection == "Foot" and outcome == "Cockroach":
            wins = countwins(wins, selection, outcome)
        elif selection == "Foot" and outcome == "Nuke":
            printlost(selection, outcome)
        elif selection == "Nuke" and outcome == "Foot":
            wins = countwins(wins, selection, outcome)
        elif selection == "Nuke" and outcome == "Cockroach":
            printlost(selection, outcome)
        elif selection == "Cockroach" and outcome == "Foot":
            printlost(selection, outcome)
        elif selection == "Cockroach" and outcome == "Nuke":
            wins = countwins(wins, selection, outcome)
        elif selection == "Q":
            break
        else:
            print("Invalid option, the input was incorrect!")
            continue
        rounds += 1
    losses = rounds - wins - ties
    print("You played",rounds,"round(s), won",wins,"time(s) and lost",losses,"time(s). There were", ties, "tie(s).")     

def printer(selection, outcome):
    print("You chose", selection)
    print("Computer got:", outcome)

def countwins(wins, selection, outcome):
    printer(selection, outcome)
    print("You WIN!")
    wins = wins + 1
    return wins

def printlost(selection, outcome):
    printer(selection, outcome)
    print("You LOSE!")

def countties(ties, selection, outcome):
    printer(selection, outcome)
    if selection == "Nuke" and outcome == "Nuke":
        print("Both LOSE!")
        return ties
    else:
        print("It's a TIE!")
        ties = ties + 1
        return ties

if __name__ == "__main__":
    main()
