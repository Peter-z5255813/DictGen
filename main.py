"""
Author: Peter Chen 2020/2021
Main function to DictGen

This file will oversee the majority of user input and is the central control

TODO
- Implement Perm function.
- Add more modules.
- Simple dictionary of common words.
- Save and load pre-existing lists.
"""

from helpers import *



def main():
    """
    main()
    
    This is the main point of user interaction and performs most of the calling for other modules
    """

    finalDict = []
    
    # These are the source list of entities. Modules will then perform permutations and store the output elsewhere
    nameList = []
    actionList = []
    dateList = []
    miscList = []
    fuzzerList = []
    
    # These flags control which modules are active or not
    leetReplacerFlag = 0
    numberFuzzerFlag = 0
    upperlowercaseFlag = 0
    datePermutationFlag = 0
    spacePermutationFlag = 0
    initFuzzerFlag = 0


    userInput = 0

    print("Welcome to DictGen, the targeted dictionary attack")
    print("Let's start by feeding in important entities")

    while True:
        print("[1] Add an entity to the source lists")
        print("[2] Remove an entity from the source lists")
        print("[3] View the source lists")    
        print("[4] Configure active modules")
        print("[5] Continue to processing")        
        userInput = input("Enter an option: ")

        # ADD handler
        if userInput == "1":
            print("What category would you consider this entity to fall under? ")
            print("[A] Name (Proper nouns)")
            print("[B] Activity")
            print("[C] Date")
            print("[D] Misc (None of the above)")
            userInput = input("Enter an option: ")
    
            if userInput == "A":
                addEntry(nameList)
            elif userInput == "B":
                addEntry(actionList)
            elif userInput == "C":
                addDate(dateList)
            elif userInput == "D":
                addEntry(miscList)
            else:
                print("Invalid input, please try again")
        
        # REMOVE handler
        elif userInput == "2":
            userInput = input("Enter the entry you would like to remove (Case sensitive): ")
            try:
                nameList.remove(userInput)
                actionList.remove(userInput)
                dateList.remove(userInput)
                miscList.remove(userInput)
            except ValueError:
                pass
            print("'" + userInput + "' has been removed")
        
        # VIEW handler
        elif userInput == "3":
            print("Here is the contents of all the lists")
            print("Names: " + str(nameList))
            print("Actions: " + str(actionList))
            print("Dates: " + str(dateList))
            print("Miscellanous: " + str(miscList))

        # MODULE handler
        elif userInput == "4":
            while True:
                print("1. initFuzzer: " + str(initFuzzerFlag))            
                print("2. leetReplacer: " + str(leetReplacerFlag))
                print("3. numberFuzzer: " + str(numberFuzzerFlag))
                print("4. upperlowercase: " + str(upperlowercaseFlag))
                print("5. datePermutation: " + str(datePermutationFlag))
                print("6. spacePermutation: " + str(spacePermutationFlag))
                print("\n7. Exit")
                        
                userInput = input("Input a number to toggle the module: ")
                if userInput == "1":
                    initFuzzerFlag = (initFuzzerFlag + 1) % 2
                elif userInput == "2":
                    leetReplacerFlag = (leetReplacerFlag + 1) % 2
                elif userInput == "3":
                    numberFuzzerFlag = (numberFuzzerFlag + 1) % 2
                elif userInput == "4":
                    upperlowercaseFlag = (upperlowercaseFlag + 1) % 2
                elif userInput == "5":
                    datePermutationFlag = (datePermutationFlag + 1) % 2
                elif userInput == "6":
                   spacePermutationFlag = (spacePermutationFlag + 1) % 2
                elif userInput == "7":
                    break
                else:
                    print("Invalid input, please try again")

        # GENERATION handler    
        elif userInput == "5":
            break
        else:
            print("Error: Invalid input, please try again")
        print("\n\n")

    print("OK! Ready to process!")
    finalDict = perm(nameList, actionList, dateList, miscList, fuzzerList)

    print("All done! Heres a preview of your custom dictionary:\n")
    print("You can find the full text in your current directory!\n")
    file = open("customDict.txt", "w")
    for i in finalDict:
        file.write(i + "\n")
        print(i)
    return





"""
CORE FUNCTIONS
============================================================
These functions provide most of the work behind the dictionary generator
as well as ensure the main function is cleaner and leaner by removing unnecessary repetition.
"""


def addEntry(specifiedList):
    userInput = input("Enter desired entity: ")
    specifiedList.append(userInput)
    print("\nSuccess!\nEntity has been added to the list: " + userInput)
    return


def addDate(specifiedList):
    newDate = []
    day = 0
    month = 0
    year = 0

    condition = True
    while condition:
        try:
            day = input("Enter day of the month: ")
            day = int(day)
            if day > 0 and day < 32:
                condition = False
            else:
                print("Error: Input out of range, please try again")
        except (TypeError, ValueError):
            print("Error: Please enter a number, please try again")
    condition = True
    while condition:
        try:    
            month = input("Enter month (number): ")
            month = int(month)
            if month > 0 and month < 13:
                condition = False
            else:
                print("Error: Input out of range, please try again")
        except (TypeError, ValueError):
            print("Error: Please enter a number, please try again")
    condition = True
    while condition:    
        try:
            year = input("Enter year (full digits): ")
            year = int(year)
            if year > 999 and year < 10000:
                condition = False
            else:
                print("Error: Input out of range, please try again")
        except (TypeError, ValueError):
            print("Error: Please enter a number, please try again")

    newDate.append(str(day))
    newDate.append(str(month))
    newDate.append(str(year))

    specifiedList.append(newDate)
    print("\nSuccess!\nEntity has been added to the list: " + str(newDate))
    return


def perm(nameList, actionList, dateList, miscList, fuzzerList):
    finalDict = []
    # First, add single, basic instances of each entity.
    listAppend(finalDict, nameList)
    listAppend(finalDict, actionList)
    listAppend(finalDict, dateList)
    listAppend(finalDict, miscList)
    listAppend(finalDict, fuzzerList)

    # Next, try to permuate within each catagory (Not all catagories are featured, just notable ones. Dates are not commonly found appended together, and fuzzerList already contains
    # notable combinations, thus should not have any additional permutations performed).
    listAppend(finalDict, concatPermutation(nameList))
    listAppend(finalDict, concatPermutation(actionList))
    listAppend(finalDict, concatPermutation(miscList))


    # TODO
    # Check for activated modules

    return finalDict


"""
ADDITIONAL MODULES
============================================================
These additional modules add unique ways to permutate source items.
Their origin comes from lots and lots of leaked password analysis!

Each module features a brief description of its purpose.

More will come in the future!
"""

def leetReplacer(word):
    '''
    This module will replace letters with its 'leet' equivalent
    '''
    # TODO
    # - Explore partial permutations
    counter = 0
    leetWord = ""
    leetDatabase = {
        "e":"3",
        "o":"0",
        "i":"1",
        "a":"4",
        "s":"5",
        "s":"z",
        "g":"6",
    }
    for c in word:
        for entry in leetDatabase:
            if c.lower() in entry:
                c = leetDatabase[c.lower()]      
        leetWord += c
        counter += 1
    return leetWord


def numberFuzzer(word):
    '''
    This module will add popular password numbers around words equivalent
    '''    
    #TODO
    return


def upperlowercase(word):
    '''
    This module will permutate for all caps, all lowers and other variations
    '''
    #TODO
    return


def datePermutation(word):
    '''
    This module will change dates to popular alternate representations
    '''
    #TODO
    return


def spacePermutation(word):
    '''
    This module will change spaces to other fillers such as hypens or underlines
    '''
    #TODO
    return


def initFuzzer(word):
    '''
    This module will initialize the fuzzer list with common password suffixes and prefixes
    '''
    #TODO
    return




if __name__ == "__main__":
    main()