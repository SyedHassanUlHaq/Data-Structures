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

