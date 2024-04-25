import sys
input = sys.stdin.readline

N, M = map(int, input().split())
knowTruth = list(map(int, input().split()))
parties = [list(map(int, input().split())) for _ in range(M)]

isKnowTruth = [0] * (N + 1)
for i in range(1, len(knowTruth)):
    isKnowTruth[knowTruth[i]] = 1

partyFlag = [1] * M
while True:
    flag = False
    for idx in range(M):
        party = parties[idx]
        for i in range(1, len(party)):
            if partyFlag[idx] and isKnowTruth[party[i]]:
                for j in range(1, len(party)):
                    isKnowTruth[party[j]] = 1
                partyFlag[idx] = 0
                flag = True
                break
    if not flag:
        break

answer = 0
for party in parties:
    if not isKnowTruth[party[1]]:
        answer += 1

print(answer)
