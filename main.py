def SIRmodel(S, I, R, contact_rate, recovery_rate):
    new_infected = contact_rate * S * I
    new_recover = recovery_rate * I

    new_S = S - new_infected
    new_I = I + new_infected - new_recoveries
    new_R = R + new_recoveries

    return new_S, new_I, new_R

def printMenu():
    print("[1] SIR Model")
    print("[0] Exit")

def getChoice(prompt):
    while(True):
        try:
            return int(input(prompt))
        except:
            print("Invalid input, try again")

def main():
    print("Hello World!")

    while True:
        printMenu()
        choice = getChoice("What is your choice: ")
        if(choice == 0):
            break
main()