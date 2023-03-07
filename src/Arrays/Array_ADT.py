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


