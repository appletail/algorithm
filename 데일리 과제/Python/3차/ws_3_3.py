infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
age = 0

for i in range(len(infos)):
    age += infos[i]['age']

print(age)