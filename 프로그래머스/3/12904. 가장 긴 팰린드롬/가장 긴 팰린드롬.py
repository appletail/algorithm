def solution(s):
    answer = 1
    for start in range(len(s)):
        for end in range(start+1, len(s)):
            if end - start < answer:
                continue
            tmp = 0
            for i in range(len(s)):
                sp = start + i
                ep = end - i
                if sp >= ep:
                    if sp == ep:
                        tmp += 1
                    answer = max(answer, tmp)
                    break
                if s[sp] == s[ep]:
                    tmp += 2
                else:
                    break
                    
    return answer
