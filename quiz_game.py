import time
import random
print("welcome to science quiz")

player = input("do u want to begin playing ? ")

if player == "yes":
    print("lets begin")

score = 0 
start_time = time.time()
questions = {
    "what is the fullform of cpu ?" : "Central Processing Unit",
    "what is the fullform of ram ?" : "Random Acess Memory",
    "what is the largest mammal of the planet earth?" : "Blue Whale",
    "what is the scientific name of the most intelligent species in earth" : "Homo Sapiens"
}
for question,answer in random.shuffle(questions.items()):
    print(question)
    ans = input()
    if ans.title() == answer:
        print("correct ans!!")
        score += 1
    else:
        print("wrong ans!")

end_time = time.time()

elapsed_time = end_time - start_time

mins = int(elapsed_time//60)
secs = int(elapsed_time%60)

print("the quiz has finally finished")

print("you did " + str(score) + " no of questions correctly out of 4 questions")

print("your percentage is", (score/4)*100)

print("time taken to complete:", mins,"mins and ", secs, "seonds")

print("thanks for playing")