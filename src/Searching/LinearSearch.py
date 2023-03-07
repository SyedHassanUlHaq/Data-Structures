def linearSearch(theValues, target):
    n = len(theValues)
    for i in range(n) :
# If the target is in the ith element , return True
        if theValues[i] == target:
            return i
    return False # If not found , return False
