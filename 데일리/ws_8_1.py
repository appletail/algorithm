participants =  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21]

match = set()
solo = set()

for i in participants:
    if i in solo:
        match.add(i)
    else:
        solo.add(i)
dugi = solo - match
dugi = list(dugi)


print(f'{participants.index(dugi[0]) + 1}번' )