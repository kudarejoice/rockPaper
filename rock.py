import random 
def rockPaperScissors():
    decision = ["Rock", "Paper", "Scissors"]
    while True:
        computer = decision[random.randint(0,2)]
        player = input("What is your choice? \n Rock \n Paper \n Scissors \n I Quit \n")
        
        if player ==  "rock":
            if computer == player:
                print("You have tied with the computer.")
            elif computer == "Paper":
                print("You loose!")
            else:
                print("You Win!")
            
        if player == "paper":
            if computer == player:
                print("You have tied with the computer.")
            elif computer == "Rock":
                print("You Win!")
            else:
                print("You loose!")
        
        if player == "scissors":
            if computer == player:
                print("You have tied with the computer.")
            elif computer == "Rock":
                print("You Lose!")
            else:
                print("You Win!")
        
        if player == "I Quit":
            print("Thank you for playing")
            break
rockPaperScissors()