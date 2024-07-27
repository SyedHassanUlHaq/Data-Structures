import array
class set:
    def __init__ (self):
        self._theElements = list()

    def __len__(self):
        return len(self._theElements)

    def __contains__(self, element):
        return element in self._theElements

    def add(self, element):
        if element not in self:
            self._theElements.append(element)
    
    def remove(self, element):
        assert element in self, "The element is not in the set"
        self._theElements.remove(element)

    def __eq__(self, setB):
        if len(self) == len(setB):
            return self.issubsetof(setB)
        else:
            return False

    def issubsetof(self, setB):
        for element in self:
            if element in setB:
                return True
            else:
                return False

    def union(self, setB):
        newSet = set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet

    def intersect(self, setB):
        newSet_1 = set()
        newSet_1._theElements.extend(self._theElements)
        for element in setB:
            if element in self:
                newSet_1._theElements.append(element)
        return newSet_1
            
    def difference(self, setB):
        newSet_2 = set()
        newSet_2._theElements.extend(self._theElements)
        for element in setB:
            if element in self:
                newSet_2._theElements.append(element)
        return newSet_2

    def __iter__(self):
        return _SetIterator(self._theElements)

class _SetIterator:
    def __init__ (self, setElements):
        self._elements = setElements
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._elements):
            element = self._elements[self._index]
            self._index += 1
            return element
        else:
            raise StopIteration

