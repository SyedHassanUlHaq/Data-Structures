import ctypes
class Array:
    def __init__(self, size):
        assert size > 0, "size must be greater than 0"
        self.size = size
        ArrayType = ctypes.py_object * size
        self.array = ArrayType()
        self.clear(None)

    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        assert index >= 0 and index < len(self.array), "index out of range"
        return self.array[index]
    
    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self.array), "index out of range"
        self.array[index] = value

    def clear(self, value1):
        for i in range(self.size):
            self.array[i] = value1
    
    def __iter__(self):
        return ArrayIterator(self.array)

class ArrayIterator:
    def __init__(self, array):
        self.theArray = array
        self.curIndex = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.curIndex < len(self.theArray):
            c = self.theArray[self.curIndex]
            self.curIndex += 1
            return c
        else:
            raise StopIteration

# A = Array(5)
# print (A.__len__())
# A.__setitem__(0, 2)
# A.__setitem__(1, 4)
# A.__setitem__(2, 6)
# A.__setitem__(3, 8)
# A.__setitem__(4, 10)
# print (A.__getitem__(0))
# print (A.__getitem__(1))
# print (A.__getitem__(2))
# print (A.__getitem__(3))
# print (A.__getitem__(4))

class Array2D:
    def __init__(self, numRow, numCols):
        self._rows = Array(numRow)
        for i in range(numRow):
            self._rows[i] = Array(numCols)

    def numRows(self):
        return len(self._rows)

    def numCols(self):
        return len(self._rows[0])

    def clear(self, value):
        for i in range(self.numRows - 1):
            for j in range(self.numCols - 1):
                self._rows.__setitem__((i, j), value)

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "invalid index"
        r = ndxTuple[0]
        c = ndxTuple[1]
        assert r >= 0 and r < self.numRows() and c >= 0 and c < self.numCols(), "ndx out of range"
        array1D = self._rows[r]
        return array1D[c]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "invalid index"
        r = ndxTuple[0]
        c = ndxTuple[1]
        assert r >= 0 and r < self.numRows() and c >= 0 and c < self.numCols(), "ndx out of range"
        array1D = self._rows[r]
        array1D[c] = value

# A = Array2D(2, 2)
# print (A.numRows())
# print(A.numCols())
# A.__setitem__((0, 0), 2)
# A.__setitem__((0, 1), 4)
# A.__setitem__((1, 0), 6)
# A.__setitem__((1, 1), 8)
# print (A.__getitem__((0, 0)))
# print (A.__getitem__((0, 1)))
# print (A.__getitem__((1, 0)))
# print (A.__getitem__((1, 1)))

class Matrix:
    def __init__(self, numRows, numCols):
        self._mat = Array2D(numRows, numCols)
        self._mat.clear(0)

    def numRows(self):
        return self._mat.numRows

    def numCols(self):
        return self._mat.numCols

    def __getitem__(self, ndxTuple):
        return self.mat[ndxTuple[0], ndxTuple[1]]

    def __setitem__(self, ndxTuple, value):
        self._mat[ndxTuple[0], ndxTuple[1]] = value

    def scaleBy (self, scalar):
        for i in range(self._mat.numRows()):
            for j in range(self._mat.numCols()):
                self._mat[i, j] *= scalar

    def transpose(self):
        self._Tmat = Matrix(self.numRows, self.numCols)
        for i in range(self._mat.numRows()):
            for j in range(self._mat.numCols()):
                self._Tmat[j, i] = self._mat[i, j]
        return self._Tmat
        
    def __add__(self, Matrix1):
        assert Matrix1.numRows() == Matrix.numRows() and Matrix1.numCols() == Matrix.numCols(), "Cannot add Matrix of different sizes"
        AddMatrix = Matrix(self.numRows, self.numCols)
        for i in range(self._mat.numRows()):
            for j in range(self._mat.numCols()):
                AddMatrix[i, j] = Matrix1[i, j] + self._mat[i, j]
        return AddMatrix

    def __sub__(self, Matrix1):
        assert Matrix1.numRows() == Matrix.numRows() and Matrix1.numCols() == Matrix.numCols(), "Cannot add Matrix of different sizes"
        SubMatrix = Matrix(self.numRows, self.numCols)
        for i in range(self._mat.numRows()):
            for j in range(self._mat.numCols()):
                SubMatrix[i, j] = Matrix1[i, j] - self._mat[i, j]
        return SubMatrix

    def __mul__(self, Matrix1):
        assert Matrix1.numRows() == Matrix.numRows() and Matrix1.numCols() == Matrix.numCols(), "Cannot add Matrix of different sizes"
        MulMatrix = Matrix(self.numRows, self.numCols)
        for i in range(self._mat.numRows()):
            for j in range(self._mat.numCols()):
                MulMatrix[i, j] = Matrix1[i, j] * self._mat[i, j]
        return MulMatrix