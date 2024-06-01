def printMenu():
    print("[0] Exit")

def getChoice(prompt):
    return int(input(prompt))

def main():
    print("Hello World!")

    while True:
        printMenu()
        choice = getChoice("What is your choice: ")
        if(choice == 0):
            break
main()