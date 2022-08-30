num = int(input())

# 반복문 사용 X

def sum_of_digit(num):
    num_lst = []
    num_lst.extend(str(num))
    num_lst = list(map(int, num_lst))

    result = sum(num_lst)

    return print(result)

sum_of_digit(num)

# 반복문 사용 O
result = 0

for i in str(num):
    result += int(i)
print(result)
