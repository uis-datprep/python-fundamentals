# Given a list iterate it and count the occurrence of each element and create a dictionary to show the count of each element
def number_counter(numbers):
    countDict = dict()
    for item in numbers:
        if (item in countDict):
            countDict[item] += 1
        else:
            countDict[item] = 1
    return countDict


# Given a following two sets find the intersection and remove those elements from the first set
def dict_intersection(set1, set2):
    intersection = set1.intersection(set2)
    return intersection


# Given a dictionary get all values from the dictionary and add it in a list but don’t add duplicates
def unique_values(dict):
    arr = list()
    for item in dict.values():
        if item not in arr:
            arr.append(item)
    return arr
