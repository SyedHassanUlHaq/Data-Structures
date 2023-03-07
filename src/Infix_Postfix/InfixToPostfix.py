import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    print("Token List: ",tokenList)
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
            print('postfixList: ',postfixList)
        elif token == '(':
            opStack.push(token)
            print('Taken is (, push into opStack: ', opStack.peek())
        elif token == ')':
            print('Taken is ), pop opStack: ')
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty ()) and (prec[opStack.peek()] >= prec[token]):
                print('opStack peek %c >= token %c, put %c in the postfixList : ' %( opStack.peek(),token ,opStack.peek()))
                postfixList.append(opStack.pop())
            opStack.push(token)
            print('token is %c, push into opStack: '%(token))
    while not opStack.isEmpty ():
        print('Stack Peek put into postfixList: ', opStack.peek())
        postfixList.append(opStack.pop())
    
    return " ".join(postfixList)

# Task 3

def evaluatePostfix(e):
# Get the length of expression
    size = len(e)
    a = 0
    b = 0
    s = Stack()
    isVaild = True
    i = 0
# work with (+,-,/,*,%) operator
    while (i < size and isVaild):
        if (e[i] >= '0' and e[i] <= '9'):
            a = ord(e[i]) - ord('0')
            s.push(a)
        elif (len(s) > 1):
            a = s.pop()
            b = s.pop()
# Perform arithmetic operations between 2 operands
            if (e[i] == '+'):
                s.push(b + a)
            elif (e[i] == '-'):
                s.push(b - a)
            elif (e[i] == '*'):
                s.push(b * a)
            elif (e[i] == '/'):
                s.push(int(b / a))
            elif (e[i] == '%'):
                s.push(b % a)
            else:
# When use other operator
                isVaild = False
        elif (len(s) == 1):
# Special case
# When use +, - at the beginning
            if (e[i] == '-'):
                a = s.pop()
                s.push(-a)
        elif (e[i] != '+'):
# When not use +,-
            isVaild = False
        else:
            isVaild = False
            i += 1
    if (isVaild == False):
# Possible case use other operators
# 1) When using special operators
# 2) Or expression is invalid
        print(e, " Invalid expression ")
        return
    print(e, " = ", s.pop())