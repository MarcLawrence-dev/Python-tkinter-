myNumList = [1, 2, 3, 4, 5]

while True:
    userInput = int(input("Enter a number:"))
    print("You are gay" if userInput in myNumList else "You are not gay " + str(userInput), end="\n")
    if userInput in myNumList:
        continue
    elif userInput == 2:
        continue
    else:
        break
