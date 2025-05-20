def solution(n, w, num):
    row = n // w + (1 if n % w else 0)
    storage = [[0] * w for _ in range(row)]
    
    switch = False
    curNum = 0
    for i in range(row-1, -1, -1):
        for j in range(w):
            curNum += 1
            if not switch:
                storage[i][j] = curNum
            else:
                storage[i][-(j+1)] = curNum
            if curNum == n:
                break
        switch = not switch
        
    for i in range(row):
        for j in range(w):
            if storage[i][j] == num:
                return i+1 if storage[0][j] else i
