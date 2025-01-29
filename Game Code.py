# Beginning with some formality like greeting and rules ....
name = input("Enter your good name please: ")

print(f"\nHello {name},\n\tWelcome to the game- Rock, Paper and Scissor.\n\n\nFor knowing the game rules enter \'Yes\' else \'No\' : ")

b = input()

# asking for rules 
if (b == 'Yes' or b == 'yes'):
    print('''Rules:-\n\tYou have to choose one of them, among rock, paper and scissor also please use numeric code for it which  
        is assigned to to them...\n\tThank You!! \n !! All the best !!\n''')

else :
    print("\nLets continue to the game.....\n")

# Main code for game ....
import random
number = [-1,0,1]
dict = {-1:"Rock",0:"Paper",1:"Scissor"}
def rps_game():
    comp_sel = random.choice(number)
    print("Choose one of them : \n-1 for Rock\n0 for Paper\n1 for Scissor \n\n Your selection : ")
    your_ans = int(input())
    
        # now some conditions for deciding who is winner....

    print(f"\n\nYour selection : {dict[your_ans]}")
    print(f"Computer selected : {dict[comp_sel]}\n")
    
    if (your_ans == comp_sel):
        print("Match Draw")

    elif ((your_ans == -1 and comp_sel == 1) or (your_ans == 0 and comp_sel == -1) or (your_ans == 1 and comp_sel == 0)):
        print(f"You Won \n Congratulations {name}!!")

    elif ((your_ans == 0 and comp_sel == 1) or (your_ans == 1 and comp_sel == -1) or (your_ans == -1 and comp_sel == 0) ):
        print(f"You Loss!! \n Try again {name}")

    else :
        print(f"{name}, you did some mistik.\n\tTry again *u*")
        rps_game()
    
    # for playing game in loop and also for exit 
    print(f"\n\nLets play again {name}! \n\n Write 'yes' to play again...   \n ENTER :- ", end="")
    a = input()

    if (a == 'Yes' or a == 'yes'):
        print("\n\n")
        rps_game()
    else :
        print(f"\nThank you for playing {name}, Hope you enjoyed...\n\n")

#function calling hehehe

rps_game()
