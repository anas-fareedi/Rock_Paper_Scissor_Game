import random 
computer = random.choice([-1,0,1])
yourchoice = input("enter your choice -> Rock , Paper , Scissor\n")

Dict ={"rock":-1,"paper":0,"scissor":1}
revDict={-1:"rock",0:"paper",1:"scissor"}
you = Dict[yourchoice]

print(f"you choose {revDict[you]} computer choose {revDict[computer]}")

if computer == you:
    print("match Draw !")
    
else:
    if you == -1 and computer == 0:
        print("computer wins")
    elif you == -1 and computer == 1:
        print("you wins !")
    
    elif you == 0 and computer == -1:
        print("computer wins !")
    elif you == 0 and computer == 1:
        print("you wins !")
        
    elif you == 1 and computer == -1:
        print("computer wins !")
    elif you == 1 and computer == 0:
        print("you wins !")
        
    else:
        print("something went wrong")
    