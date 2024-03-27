def solution(friends, gifts):
    answer = 0
    friendDict = {friends[i]: {friend: 0 for friend in friends} for i in range(len(friends))}
    giftPoint = {friend: {'give': 0, 'take': 0, 'point': 0} for friend in friends}
    
    for gift in gifts:
        give, take = gift.split(' ')
        friendDict[give][take] += 1
        giftPoint[give]['give'] += 1
        giftPoint[give]['point'] = giftPoint[give]['give'] - giftPoint[give]['take']
        giftPoint[take]['take'] += 1
        giftPoint[take]['point'] = giftPoint[take]['give'] - giftPoint[take]['take']
    
    for me in friends:
        takeNextMonth = 0
        for friend in friends:
            giveAndtakeRecord = friendDict[me][friend] - friendDict[friend][me]
            if giveAndtakeRecord > 0:
                takeNextMonth += 1
            elif giveAndtakeRecord == 0 and giftPoint[me]['point'] > giftPoint[friend]['point']:
                takeNextMonth += 1
            answer = max(answer, takeNextMonth)
        
    return answer