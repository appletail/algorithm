int_list = list(map(int, input()[1:- 1].split(',')))
result = [int_list[0]]

for i in range(len(int_list) - 1):
    if int_list[i] != int_list[i + 1]:
        result.append(int_list[i + 1])

print(result)

# 기존 코드
# for i in range(len(int_list) - 1):
#     if int_list[i] == int_list[i + 1]:
#         continue
#     else:
#         result.append(int_list[i + 1])

# print(result)