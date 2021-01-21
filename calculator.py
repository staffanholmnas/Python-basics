# Calculator
import math

def givenumbers():
    while True:
        number = input("Give a number: ")
        try: number = int(number)
        except Exception: print("Invalid input.")
        else: break
    return number   

print("Calculator")
number1 = givenumbers()
number2 = givenumbers()
while True:
    print()
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5) sin(number1/number2)")
    print("(6) cos(number1/number2)\n(7)Change numbers\n(8)Quit")
    print("Selected numbers:", number1, number2)
    operator = input("Please select an operation (1-8):")
    if operator.isdigit(): operator = int(operator)
    if operator == 1: print("The result is:", number1 + number2)
    elif operator == 2: print("The result is:", number1 - number2)
    elif operator == 3: print("The result is:", number1 * number2)
    elif operator == 4: print("The result is:", number1/number2) if number2 != 0 else print("Can't divide by zero!")
    elif operator == 5: print("The result is:", math.sin(number1/number2)) if number2 != 0 else print("Can't divide by zero!")
    elif operator == 6: print("The result is:", math.cos(number1/number2)) if number2 != 0 else print("Can't divide by zero!")
    elif operator == 7:
        number1 = givenumbers()
        number2 = givenumbers()
    elif operator == 8:
        print("Thank you, goodbye!")
        break
    else: print("Invalid selection.")