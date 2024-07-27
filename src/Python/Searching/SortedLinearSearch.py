def sortedLinearSearch(theValues, item):
    n = len(theValues)
    for i in range(n) :
# If the target is found in the ith element , return True
        if theValues[i] == item:
            return i
        elif theValues[i] > item:
            return False
    return False # The item is not in the sequence.
