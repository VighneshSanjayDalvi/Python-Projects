import random
computer=0
user = 0 

Userchoice = int(input("Enter 1- Stone , 2 - Paper, 3- Scirrors : "))

ComputerSection = random.randint(1,3)

# print(COmputerSection)

if (Userchoice == ComputerSection):
    print("Draw")
else:
    if(ComputerSection== 1):
        ComputerSelected = "Stone"
        match Userchoice:
            case 2:
                print("WIN",'Computer Selected ->',ComputerSelected)
            case 3:
                print("LOSE",'Computer Selected ->',ComputerSelected)
    elif(ComputerSection== 2):
        ComputerSelected = "Paper"
        match Userchoice:
            case 1:
                print("LOSE",'Computer Selected ->',ComputerSelected)
            case 3:
                print("WIN",'Computer Selected ->',ComputerSelected)
    elif(ComputerSection == 3):
        ComputerSelected = "Scissors" 
        match Userchoice:
            case 1:
                print("WIN",'Computer Selected ->',ComputerSelected)
            case 2:
                print("LOSE",'Computer Selected ->',ComputerSelected)
    else:
        print("Oops! You entered wrong")
    
