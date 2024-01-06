def countOnes(n):
    ones = 0
    
    while n > 0:
        if n % 2 == 1:
            ones += 1
        n //= 2
        
    return ones
        

def solution(n):
    answer = 0
    nOnes = countOnes(n)
    for i in range(n + 1, 1_000_001):
        if countOnes(i) == nOnes:
            return i
