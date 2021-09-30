class Riddle:

    def __init__(self, activate, correctAnswer):
        self.activate = activate
        self.correctAnswer = correctAnswer

    def activate(Self):
        print("Welcome")
        print("You are locked in this room...")
        print("To proceed to the next room you have to answer this question correct.")
        
    def correctAnswer(self):
        self.correctAnswer
        answer = input().lower()
        while True:
            if answer == self.correctAnswer:
                print("Your answer is correct you may now proceed to the next room!")
                break
            else:
                print("Your answer is wrong please try again...")
                continue

r1 = Riddle("What is the name of greatest videogame\n",
            "ever created\n",
            "is it, Skyrim, Assassins Creed or World of Warcraft.", correctAnswer = 'skyrim')

r2 = Riddle("There was a famous viking king who lived during the 9th century.\n",
            "His lastname is used as the name for a wireless connection technique (Bluetooth).\n",
            "But what was his firstname.\n",
            "Was it Harald, Ragnar or Olof\n", correctAnswer = 'harald')

r3 = Riddle("A man who was outside in the rain without an umbrella or hat didn't get a single hair on his head wet. Why?\n",
            "'He was running', 'he was bald' or 'he was already wet'\n", correctAnswer =  'he was bald')

r4 = Riddle("The more of this there is, the less you see. What is it?\n",
            "Is it, 'Trees' or 'Darkness'?\n", correctAnswer = 'darkness')

r5 = Riddle("What is always infront of you but can't be seen?\n",
            "the future, a fast animal or the sun: \n", correctAnswer = 'the future')