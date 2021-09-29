
class RiddleNrFive:

    def __init__(self):
        pass
    
    def riddle5(self):
        while True:
            print("Welcome!")
            print("You are locked in this room you can leave when you answer this riddle correctly.")
            print("Riddle: The more of this there is, the less you see. What is it?")
            print("Is it, A. Trees or B. Darkness?")

            answer = input().lower()

            if answer == 'trees':
                print("You are wrong try again...")

            elif answer == 'darkness':
                print("You are correct you may now proceed to the next room!")
                break