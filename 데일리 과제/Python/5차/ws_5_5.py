words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}

words_dict = sorted(words_dict)

for i in range(len(words_dict)):
    if words_dict[i][0] in ('b', 'm', 'p'):
        words_dict[i] = 'im' + words_dict[i]
    elif words_dict[i][0] == 'l':
        words_dict[i] = 'il' + words_dict[i]
    elif words_dict[i][0] == 'r':
        words_dict[i] = 'ir' + words_dict[i]

words_dict = sorted(words_dict)

for j in range(len(words_dict)):
    print(words_dict[j], end = ', ')