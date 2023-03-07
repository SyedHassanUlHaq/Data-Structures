class Postfix_Calculator:
    def __iniit__(self):
        self.operandstack = stack()
        self.savestack = stack()

    def value(self, a):
        self.operandstack.push(a)
    
    def result(self):
        assert not self.operandStack.isEmpty(), "Empty stack"
        return self.operandstack.peek()

    def clear(self):
        for i in range(len(self.operandstack)):
            self.operandstack.pop()
        for i in range(len(self.savestack)):
            self.savestack.pop()

    def clearLast(self):
        assert not self.operandstack.isEmpty(), "Empty stack"
        self.operandstack.pop()
    
    def compute(self, opr):
        assert not self.operandstack.isEmpty(), "Empty stack"
        assert len(self.operandstack) >= 2, "Not enogh operands"
        b = self.operandstack.pop()
        a = self.operandstack.pop()
        if opr == "*":
            self.operandstack.push(a * b)
        elif opr == "-":
            self.operandstack.push(a - b)
        elif opr == "+":
            self.operandstack.push(a + b)
        elif opr == "/":
            self.operandstack.push(a / b)
        elif opr == "**":
            self.operandstack.push(a ** b)
        elif opr == 'abs':
            self.operandstack.push(abs(a))
        elif opr == 'sqrt':
            self.operandstack.push(sqrt(a))
        elif opr == 'sin':
            self.operandstack.push(sin(a))
        elif opr == 'cos':
            self.operandstack.push(cos(a))
        elif opr == 'tan':
            self.operandstack.push(tan(a))
        else:
            assert False, "Invalid operation"

    def store(self):
        assert not self.operandstack.isEmpty(), "Empty stack"
        self.savestack.push(self.operandstack.pop())

    def recall(self):
        assert not self.savestack.isEmpty(), "Empty stack"
        self.operandstack.push(self.savestack.pop())
