class RiddleNrTwo:

    def __init__(self):
        pass
    
    def riddle2(self):
        while True:
            print("Welcome")
            print("To proceed to the next room you have to answer this question correct.")
            print("During World War II during the battle of Normandy D-Day to be exact")
            print("The americans landed on two beaches, what was the names of those two beach heads?")
            print("Was it Omaha and Utah, Gold and Sword or was it Juno and Pluto")

            answer = input().lower()

            if answer == 'omaha and utah':
                print("Your answer is correct you may now proceed to the next room!")
                break
            elif answer == 'gold and sword':
                print("Your answer is incorrect, the british landed on those two beaches")
            elif answer == 'juno and pluto':
                print("Your answer is incorrect, it was the canadians who landed on the beach Juno and Pluto is not even a beach i Normandy")