import operator

def reverseDirection(direction: str):
    if direction == "n":
        return "s"
    elif direction == "e":
        return "w"
    elif direction == "s":
        return "n"
    elif direction == "w":
        return "e"
    else:
        print("Error: Invalid direction.")
        return False

def doubleRange(x_max: int, y_max: int):
    intPairList = []

    for x in range(x_max):
        for y in range(y_max):
            intPairList.append([x, y])

    return intPairList

def listSubtraction(minuendList: list, subtrahendList: list):
    
    for subtrahend in subtrahendList:
        try:
            minuendList.remove(subtrahend)
        except:
            pass

def listOfPairs(list1: list, list2: list):
    pairList = []

    for list1Element in list1:
        for list2Element in list2:
            pairList.append([list1Element, list2Element])

    return pairList


