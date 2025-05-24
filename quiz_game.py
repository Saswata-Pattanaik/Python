import time
import random

class quiz():
    def __init__(self):
        self.questions = {
             "What is the full form of CPU?" : "Central Processing Unit",
            "What is the full form of RAM?" : "Random Access Memory",
            "What is the largest mammal on planet Earth?" : "Blue Whale",
            "What is the scientific name of the most intelligent species on Earth?" : "Homo Sapiens"
        }
        self.score = 0
        self.start_time = None
        self.end_time = None
    
    def start(self):
        print("welcome to quiz")
        player_state = input("do u wanna play (Yes/no) ? ")
        if player_state != "yes" :
            print("maybe next time! begin")
            return
        print("let's begin")
        self.start_time = time.time()
        self.ask_questions()
        self.end_time = time.time()
        self.show_results()

    def ask_questions(self):
        question_list = list(self.questions.items())
        random.shuffle(question_list)

        for question,answer in question_list:
            print(question)
            ans = input("whats your answer ?")
            if ans.strip().lower() == answer:
                print("correct answer!!")
                self.score += 1
            else:
                print("wrong answer! the correct answer is", answer)

    def show_results(self):
        print("score of the player is,", self.score)
        elapsed_time = self.end_time - self.start_time
        mins = int(elapsed_time//60)
        secs = int(elapsed_time%60)

        print("quiz succesfully completed")
        print("time taken to complete", mins,"mins", secs, "secs")
        print("score obtained: ", self.score )
    
if __name__ == "__main__":
    Quiz = quiz()
    Quiz.start()
