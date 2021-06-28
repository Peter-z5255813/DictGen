"""
Author: Peter Chen 2020/2021
Main function to DictGen

This file will oversee the majority of user input and is the central control
"""

def main():
        



    nameList = []
    actionList = []
    dateList = []
    miscList = []

    fuzzerList = []


    userInput = 0


    print("Welcome to DictGen, the targeted dictionary attack")
    print("Let's start by feeding in important entities")

    while True:
        print("[1] Add an entity to our lists")
        print("[2] Remove an entity from our lists")    
        print("[3] Continue to processing")
        userInput = input("Enter an option: ")
        if userInput == "1":
            print("\n")
            print("What catagory would you consider this entity to fall under? ")
            print("[1] Name (Proper nouns)")
            print("[2] Activity")
            print("[3] Date")
            print("[4] Misc (None of the above)")
            userInput = input("Enter an option: ")
    
            if userInput == "1":
                addEntry(nameList)
            elif userInput == "2":
                addEntry(actionList)
            elif userInput == "3":
                addEntry(dateList)
            elif userInput == "4":
                addEntry(miscList)
            else:
                print("Invalid input, please try again")
        
        elif userInput == "2":
            userInput = input("Enter the entry you would like to remove (Case sensitive): ")
            try:
                nameList.remove(userInput)
                actionList.remove(userInput)
                dateList.remove(userInput)
                miscList.remove(userInput)
            except ValueError:
                pass
        elif userInput == "3":
            break
        else:
            print("Invalid input, please try again")
        print("\n")

    print("Ready to process!")
    finalDict = perm(nameList, actionList, dateList, miscList, fuzzerList)

    print("Done! Heres your custon dictionary:\n")
    for i in finalDict:
        print(i)

    return


def addEntry(specifiedList):
    userInput = input("Enter desired entity: ")
    specifiedList.append(userInput)
    print("\nSuccess!\nEntity has been added to the list: " + userInput)
    return


def perm(nameList, actionList, dateList, miscList, fuzzerList):
    finalDict = []

    for i in nameList:
        finalDict.append(i)
    for i in actionList:
        finalDict.append(i)
    for i in dateList:
        finalDict.append(i)
    for i in miscList:
        finalDict.append(i)
    for i in fuzzerList:
        finalDict.append(i)                        
    return finalDict


'''
This module will replace letters with its 'leet' equivalent
'''
def replacer(word):
    return


'''
This module will add popular password numbers around words equivalent
'''
def numberFuzzer(word):
    return

'''
This module will permutate for all caps, all lowers and other variations
'''
def upperlowercase(word):
    return

'''
This module will change dates to popular permutations
'''
def datePermuator(word):
    return

#TODO
# Add more modules
# -simple dictionary


if __name__ == "__main__":
    main()