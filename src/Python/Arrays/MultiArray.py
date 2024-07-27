
class multiArray:
    def __init__(self, *dimensions):
        assert len(dimensions) > 1, "Dimensions can not be less than 1"
        self.dim = dimensions
        size = 1
        for d in dimensions:
            assert d> 0, "Dimensions should be greater than "
            size *= d
        
        self._elements = array(size)
        self._factors = array(len(dimensions))
        self._computeFactors()

    def numDims(self):
        return len(self._dims)

    def length(self, dim):
        assert dim >= 1 & dim <= len(self._dims), "//"
        return self._dims[dim - 1]

    def clear(self, value):
        self._elements.clear(value)

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == self.numDims(), "invalid array subscript"
        index = self._computeIndex(ndxTuple)
        assert index is not None,"Array subscript out of range"
        return self._elements[index]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == self.numDims(), "invalid number of array subscripts"
        index = self._computeIndex(ndxTuple)
        assert index is not None, "Array subscript out of range"
        self._elements[index] = value

    def _computeIndex(self, idx):
        offset = 0
        for j in range(len(idx)):
            if idx[j] < 0 or idx[j] >= self._dims[j]:
                return None
            else:
                offset += idx[j] * self._facttors[j]
                return offset
    
    def _computeFactors(self):
        self._factors[len(self._factors) - 1] = 1
        for j in reversed(range(len(self._factors) - 1)):
            self._factors[j] = self._factors[j + 1] *self._dims[j + 1]

            
