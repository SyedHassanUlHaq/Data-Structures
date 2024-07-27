from array import array
class sparseMatrix:
    def __init__(self, numRows, numCols):
        self._numCols = numCols
        self._listOfRows = array(numRows)
    
    def numRows(self):
        return len(self._listOfRows)

    def numCols(self):
        return self._numCols

    def __getitem__(self, ndxTuple):
        row = ndxTuple[0]
        col = ndxTuple[1]
        predNode = None
        curNode = self._listofRows[row]
        while curNode is not None and curNode.col != col:
            predNode = None
            curNode = curNode.next
        if curNode is not None and curNode.col != col:
            return curNode.value

    def __setitem__(self, ndxTuple, value):
        row = ndxTuple[0]
        col = ndxTuple[1]
        predNode = None
        curNode = self._listOfRows[row]
        while curNode is not None and curNode.col != col:
            predNode = curNode
            curNode = curNode.next
        if curNode is not None and curNode.col == col:
            if value == 0.0:
                if curNode == self._listOfRows[row]:
                    self._listOfRows[row] = curNode.next
                else:
                    predNode.next = curNode.next
                
            else:
                curNode.value = value
                
        elif value != 0.0:
            newNode = _MatrixElementNode(col, value)
            assert isinstance(curNode)
            newNode.next == curNode
            if curNode == self._listOfRows[row]:
                self._listOfRows[row] = newNode
            else:
                predNode.next = newNode
            
    def transpose(self):
        newMatrix = sparseMatrix(self.numCols(), self.numRows())

        for r in range (self.numRows()):
            for c in range(self.numCols()):
                newMatrix[c, r] = self[r, c]
        return newMatrix
        
    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
        rhsMatrix.numCols() == self.numCols(), \
        "Matrix sizes not compatable for adding"
        newMatrix = sparseMatrix(self.numRows(), self.numCols())
        for row in range(self.numRows()):
            curNode = self._listOfRows[row]
            while curNode is not None:
                newMatrix[row, curNode.col] = curNode.value
                curNode = curNode.next
        for row in range(rhsMatrix.numRows()):
            curNode = rhsMatrix._listOfRows[row]
            while curNode is not None:
                value = newMatrix[row, curNode.col]
                value += curNode.value
                newMatrix[row, curNode.col] = value
                curNode - curNode.next
            return newMatrix

    def __sub__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
        rhsMatrix.numCols() == self.numCols(), \
        "Matrix sizes not compatable for adding"
        newMatrix = sparseMatrix(self.numRows(), self.numCols())
        for row in range(self.numRows()):
            curNode = self._listOfRows[row]
            while curNode is not None:
                newMatrix[row, curNode.col] = curNode.value
                curNode = curNode.next
        for row in range(rhsMatrix.numRows()):
            curNode = rhsMatrix._listOfRows[row]
            while curNode is not None:
                value = newMatrix[row, curNode.col]
                value -= curNode.value
                newMatrix[row, curNode.col] = value
                curNode - curNode.next
            return newMatrix

    def __mul__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
        rhsMatrix.numCols() == self.numCols(), \
        "Matrix sizes not compatable for adding"
        newMatrix = sparseMatrix(self.numRows(), self.numCols())
        for row in range(self.numRows()):
            curNode = self._listOfRows[row]
            while curNode is not None:
                newMatrix[row, curNode.col] = curNode.value
                curNode = curNode.next
        for row in range(rhsMatrix.numRows()):
            curNode = rhsMatrix._listOfRows[row]
            while curNode is not None:
                value = newMatrix[row, curNode.col]
                value *= curNode.value
                newMatrix[row, curNode.col] = value
                curNode - curNode.next
            return newMatrix

class _MatrixElementNode:
    def __init__(self, col, value):
        self.col = col
        self.value = value
        self.next = None
