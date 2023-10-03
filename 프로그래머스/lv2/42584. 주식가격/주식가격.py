def solution(prices):
    length = len(prices)
    answer = [0] * length
    
    for i in range(length):
        second = 0
        for j in range(i + 1, length):
            second += 1
            if prices[i] > prices[j]:
                break
                
        answer[i] = second
        
    return answer
