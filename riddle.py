class Riddle:

    def __init__(self, question, correctAnswer, timesToTry):
        self.question = question
        self.correctAnswer = correctAnswer
        self.timesToTry = timesToTry

    def activate(self):
        print("Welcome")
        print("You are locked in this room...")
        print("To proceed to the next room you have to answer this riddle correct.")
        print("For each riddle you will have a number of tries to answer correct.")
        print("The number of tries are diffrent for each riddle.")
        print("Be aware if you answer incorrectly you will be sent back to the beginning of the game.")
        print("So think before you answer.")
        
        print(self.question)

        tries = 0
        while tries < self.timesToTry:
            answer = input().lower()
            if answer == self.correctAnswer:
                break
            elif answer != self.correctAnswer:
                print("Your answer is incorrect try again.")
                tries += 1
        
        if tries == self.timesToTry:
            print("You have answered incorrectly two times you will now be sent back.")
            return False
        else:
            print("Your answer is correct you may now proceed to the next room!")
            return True
        
    def answer(self):
        self.correctAnswer

r1 = Riddle("What is the name of greatest videogame\n"
            "ever created\n"
            "is it, Skyrim, Assassins Creed or World of Warcraft.", correctAnswer = 'skyrim', timesToTry = 3)

r2 = Riddle("There was a famous viking king who lived during the 9th century.\n"
            "His lastname is used as the name for a wireless connection technique (Bluetooth).\n"
            "But what was his firstname.\n"
            "Was it Harald, Ragnar or Olof\n", correctAnswer = 'harald', timesToTry = 2)

r3 = Riddle("A man who was outside in the rain without an umbrella or hat didn't get a single hair on his head wet. Why?\n"
            "'He was running', 'he was bald' or 'he was already wet'\n", correctAnswer =  'he was bald', timesToTry = 2)

r4 = Riddle("The more of this there is, the less you see. What is it?\n"
            "Is it, 'Trees' or 'Darkness'?\n", correctAnswer = 'darkness', timesToTry = 1)

r5 = Riddle("What is always infront of you but can't be seen?\n"
            "the future, a fast animal or the sun: \n", correctAnswer = 'the future', timesToTry = 2)

r6 = Riddle("I have keys but no locks, and space and no rooms\n"
            "you can enter but you can't go outside, what am i?"
            "This riddle has a one word answer", correctAnswer = 'keyboard', timesToTry = 30)