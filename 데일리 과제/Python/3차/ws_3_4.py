blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']


# blood_count = {}

# for i in blood_types:
#     if i in blood_count:
#         blood_count[i] += 1
#     else:
#         blood_count[i] = 1
# print(blood_count)



def myFunc(lst):
    result = {}

    bloods = ['A', 'B,', 'AB', 'O']
    for type in bloods:
        result[type] = lst.count(type)

    return result


print(myFunc(blood_types))