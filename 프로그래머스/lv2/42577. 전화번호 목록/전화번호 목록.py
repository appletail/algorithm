from collections import defaultdict

def solution(phone_book):
    phones = defaultdict(int)
    for i in phone_book:
        phones[i] = 1
    
    for phone in phone_book:
        num = ''
        for s in phone:
            num += s
            if num != phone and phones[num]:
                return False
            
    return True