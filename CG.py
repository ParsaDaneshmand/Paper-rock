from secrets import choice
paper= "paper"
rock= "rock"
scissor= "scissor"
game= ["paper" , "rock" , "scissor"]
pc= (choice(game))
print("your weapons are", (game))
game_count= i= 0 
while game_count<3:
    player= input("choose a weapon: ")
    game_count+=1
    if player==pc:
        print('draw')
    elif player== rock and paper== pc or player== scissor and rock== pc or player== paper and scissor== pc:
        print("you lost")
    else:
        print("you win")
