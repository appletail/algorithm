def solution(temperature, t1, t2, a, b, onboard):
    outsideTemp = temperature + 10
    minGoodTemp = t1 + 10
    maxGoodTemp = t2 + 10
    
    dp = [[1e9] * 52 for _ in range(len(onboard))]
    dp[0][outsideTemp] = 0
    for time in range(1, len(onboard)):
        passenger = onboard[time]
        
        considerMinTemp, considerMaxTemp = minGoodTemp, maxGoodTemp
        if not passenger:
            considerMinTemp, considerMaxTemp = min(minGoodTemp, outsideTemp), max(maxGoodTemp, outsideTemp)
        
        for temp in range(considerMinTemp, considerMaxTemp + 1):
            if temp == outsideTemp:
                dp[time][temp] = min(dp[time - 1][temp - 1], dp[time - 1][temp], dp[time - 1][temp + 1])
            elif temp > outsideTemp:
                dp[time][temp] = min(dp[time - 1][temp - 1] + a, dp[time - 1][temp] + b, dp[time - 1][temp + 1])
            elif temp < outsideTemp:
                dp[time][temp] = min(dp[time - 1][temp - 1], dp[time - 1][temp] + b, dp[time - 1][temp + 1] + a)

    return min(dp[-1])