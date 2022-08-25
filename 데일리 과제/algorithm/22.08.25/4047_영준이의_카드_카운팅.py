import sys
sys.stdin = open("input.txt", "r")


def check(card):
    s = []; d = []; h = []; c = []
    for i in range(0, len(card), 3):
        if card[i] == 'S':
            if int(card[i + 1: i + 3]) in s:
                return 'ERROR'
            else:
                s.append(int(card[i + 1: i + 3]))
        elif card[i] == 'D':
            if int(card[i + 1: i + 3]) in d:
                return 'ERROR'
            else:
                d.append(int(card[i + 1: i + 3]))
        elif card[i] == 'H':
            if int(card[i + 1: i + 3]) in h:
                return 'ERROR'
            else:
                h.append(int(card[i + 1: i + 3]))
        elif card[i] == 'C':
            if int(card[i + 1: i + 3]) in c:
                return 'ERROR'
            else:
                c.append(int(card[i + 1: i + 3]))
    return [13 - len(s), 13 - len(d), 13 - len(h), 13 - len(c)]


T = int(input())

for test_case in range(1, T + 1):
    cards = input()
    if check(cards) == 'ERROR':
        print(f'#{test_case}', check(cards))
    else:
        print(f'#{test_case}', *check(cards))


