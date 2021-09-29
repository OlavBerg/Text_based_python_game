class RiddleNrFour:

    def __init__(self):
        pass
    
    def riddle4(self):
        while True:
            print("Welcome")
            print("To proceed to the next room you have to answer this riddle.")
            print("A man who was outside in the rain without an umbrella or hat didn't get a single hair on his head wet. Why?")
            print("A. He was running, B. he was bald, C. he was already wet")

            answer = input().lower()

            if answer == 'he was running':
                print("Your answer is wrong, try again...")
            elif answer == 'he was bald':
                print("You are correct you may now proceed to the next room!")
                break
            elif answer == 'he was already wet':
                print("Your answer is wrong, try again...")

