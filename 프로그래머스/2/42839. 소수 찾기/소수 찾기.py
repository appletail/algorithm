import math
from itertools import permutations

def isPrime(num):
    if num == 0 or num == 1:
        return 0
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 1

def makeNum(numbers, count, used, curNum):
    if curNum:
        num = int("".join(curNum))
        count[num] = isPrime(num)
        
    for i in range(len(numbers)):
        if not used[i]:
            used[i] = 1
            curNum.append(numbers[i])
            makeNum(numbers, count, used, curNum)
            used[i] = 0
            curNum.pop()
        
        
def solution(numbers):
    count = [0] * 10000000
    used = [0] * len(numbers)
    makeNum(numbers, count, used, [])
    
    return sum(count)