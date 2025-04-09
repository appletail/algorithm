def findN(word):
    n = 0
    for i in range(1, len(word)+1):
        n += (ord(word[-i]) - ord('a') + 1) * (26 ** (i-1))
    return n

def mkWord(n, lst):
    a = n // 26
    b = n % 26
    lst.append(b)
    if a == 0 :
        return lst
    else :
        return mkWord(a-1, lst)

def solution(n, bans):
    answer = ''
    # bans에 들어있는 글자의 위치를 확인
    # bans의 글자 위치 중 n보다 앞에 있는 글자들 수 만큼 n에 가산
    # 위의 절차를 n보다 앞에 있는 글자가 없어질때 까지 반복
    # 그렇게 구한 n번째 글자 return
    # a 1 aa 27 ba 53
    bans = sorted(bans, key=lambda x: [len(x), x])
    existBans = []
    for ban in bans:
        if findN(ban) <= n:
            n += 1

    tmp = []
    mkWord(n-1, tmp)
    while tmp:
        answer += chr(ord('a') + tmp.pop())
    
    return answer
