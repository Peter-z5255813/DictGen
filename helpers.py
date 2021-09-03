"""
Author: Peter Chen 2020/2021
Helper functions for DictGen

This contains common functions and modules that are repeatedly used,
kept and localised in this file to ensure clean and consistent code

"""


def listAppend(list1, list2):
    """
    listAppend(list1, list2)
    
    Each item in `list2` is appended to `list1`.
    """
    for i in list2:
        list1.append(i)
    return list1

def concatPermutation(list1):
    """
    concatPermutation(list1)
    
    Every possible pair is generated with the items in `list1` (excluding duplicate names)
    then added to `newList` which is returned.
    """
    newList=[]
    for i in list1:
        for j in list1:
            if i == j:
                continue
            oneWordRepresentation = i + j
            newList.append(oneWordRepresentation)
    
    return newList