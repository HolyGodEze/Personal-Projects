from classList import *

def mainMenu():
    print("Welcome to the RPG Battle Simulator!")
    print("1. Start Game")
    print("2. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("Starting game...")
        # Here you would call the function to start the game
    elif choice == '2':
        print("Exiting game. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        mainMenu()
        
def startGame():
    pass

def classSelect():
    print("Choose your class below:")
    print("1. Piercer")
    print("2. Back to Main Menu")
    if input() == 1:
        print(Piercer())
    