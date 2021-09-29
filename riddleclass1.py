class RiddleNrOne(Riddle):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    
    def riddleNr1(self):
        while True:
            print("To proceed to the next room you have to answer this riddle correct...")
            print("What is always infront of you but can't be seen?")
            print("A. the future, B. a fast animal, C. the sun: ")
            answer = input().lower()

            if answer == 'a':
                print("You are correct you may now proceed to the next room!")
                break
            elif answer == 'b':
                print("Your answer is wrong, please try again...")
            elif answer == 'c':
                print("Your answer is wrong, please try again...")






