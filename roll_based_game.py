import random

def no_of_players():
    while True:
        np = input("enter no of players: ")
        try:
            np = int(np)
            if np <= 0:
                print("please enter a number bigger than zero")
            else:
                break

        except ValueError as e:  
            print("please enter a number ") 
        
    return np


np = no_of_players()

def roll_dice():
    num = random.randint(1,6)
    return int(num)

scores = []
score = 0

if __name__ == "__main__":
    print("you can choose any no of rounds to play but if you get 1 on dice all your previous score would be reverted to 0 and your turn is terminated")
    for i in range(0,np):
        print("player", i , "turn: ")
        cond = int(input("please enter the no of turns you want to play: "))
        for j in range(1,cond+1):
            num = roll_dice()
            print(j,")", 'you get', num)
            if num != 1:
                score += num
            else:
                score = 0
                break
        scores.append(score)
        score = 0
        
    
    print("game finished")
    print("final scores are as follows:")

    for i in range(0,len(scores)):
        print("player", i, 'scored', scores[i])
