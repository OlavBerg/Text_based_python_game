class RiddleNrThree:

    def __init__(self):
        pass
    
    def riddle3(self):
        while True:
            print("Welcome")
            print("To proceed to the next room you have to answer the the question correct.")
            print("There was a famous viking king who lived during the 9th century.")
            print("His lastname is used as the name for a wireless connection technique (Bluetooth).")
            print("But what was his firstname.")
            print("Was it A. Harald, B. Ragnar, C. Olof")

            answer = input().lower()

            if answer == 'harald':
                print("You are correct the wireless connection Bluetooth is named after Harald Blåtand king of Denmark, you may proceed to the next room!")
                break
            elif answer == 'ragnar':
                print("Your answer is wrong, Ragnar Lothbrok was another viking leader but not the one this question is looking for, try again...")
            elif answer == 'olof':
                print("You are wrong, Olof is Olof SKötkonung one of the first swedish kings, try again...")

