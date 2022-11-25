blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

result = {}
for typ in blood_types:
    if typ in result:
        result[typ] += 1
    else:
        result[typ] = 1
print(result)
