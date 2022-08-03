def fn_d(n):
    result = 0

    num = str(n)
    for i in num:
        result += int(i)
    result += n

    return result


def is_selfnumber(n):
    for i in range(n):
        if fn_d(i) == n:
            return False
    return True


print(is_selfnumber(14316))

# def is_selfnumber(n):

#     self_number = set(i+1 for i in range(n))

#     not_self_number  = set()

#     for i in range(1, n+1):
#         not_self_number.add(fn_d(i))

#     self_number = self_number - not_self_number

#     return self_number