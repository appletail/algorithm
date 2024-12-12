def findNary(num):
    maxNum = 0
    while num > 0:
        curNum = num % 10
        num //= 10
        maxNum = max(maxNum, curNum)
    
    return maxNum + 1

def calculate(A, operator, B):
    if operator == "+":
        return A + B
    elif operator == "-":
        return A - B

def toNary(num, nary):
    if num == 0:
        return "0"
    naryNum = ""
    while num > 0:
        naryNum = str(num % nary) + naryNum
        num //= nary
    return naryNum

def solution(expressions):
    answer = []
    expressions = list(map(lambda x: x.split(" "), expressions))
    minNary = 2
    for expression in expressions:
        for i in expression:
            if i.isdecimal():
                minNary = max(minNary, findNary(int(i)))

    naries = [0] * 10
    for expression in expressions:
         if expression[4] != "X":
                for nary in range(minNary, 10):
                    DecimalA = int(expression[0], nary)
                    DecimalB = int(expression[2], nary)
                    DecimalC = int(expression[4], nary)
                    
                    DecimalTmp = calculate(DecimalA, expression[1], DecimalB)
                    
                    if DecimalTmp == DecimalC:
                        naries[nary] += 1

    curNary = minNary
    naryFlag = False
    naryCnt = 0
    for i in range(len(naries)):
        nary = naries[i]
        if naryCnt < nary:
            naryCnt = nary
            naryFlag = True
            curNary = i
        elif naryCnt == nary:
            naryFlag = False
    
    for expression in expressions:
        if expression[4] == "X":
            if naryFlag:
                DecimalA = int(expression[0], curNary)
                DecimalB = int(expression[2], curNary)
                DecimalTmp = calculate(DecimalA, expression[1], DecimalB)
                answer.append(f"{expression[0]} {expression[1]} {expression[2]} {expression[3]} {toNary(DecimalTmp, curNary)}")
            else:
                XFlag = False
                curX = 0
                for nary in range(minNary, 10):
                    DecimalA = int(expression[0], nary)
                    DecimalB = int(expression[2], nary)
                    DecimalTmp = calculate(DecimalA, expression[1], DecimalB)
                    tmp = toNary(DecimalTmp, nary)
                    
                    if not XFlag:
                        XFlag = True
                        curX = tmp
                    elif tmp != curX:
                        XFlag = False
                        break
                if XFlag:
                    answer.append(f"{expression[0]} {expression[1]} {expression[2]} {expression[3]} {curX}")
                else:
                    answer.append(f"{expression[0]} {expression[1]} {expression[2]} {expression[3]} ?")
        
    return answer
