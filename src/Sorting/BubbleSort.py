def bubbleSort(theSeq):
    n = len(theSeq)
    # Perform n-1 bubble operations on the sequence
    for i in range( n - 1 ) :
    # Bubble the largest item to the end.
        for j in range(n - i - 1) :
            if theSeq[j] > theSeq[j + 1] : # swap the j and j+1 items.
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
    return theSeq
