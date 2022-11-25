def sum_of_repeat_number(num_list):
    one = []
    more = []

    for num in num_list:
        if num in one or num in more:
            more.append(num)
            if num in one:
                one.remove(num)
        
        else:
            one.append(num)
    result = sum(one)

    return result


nlist = [4, 4, 7, 8, 10, 4]
print(sum_of_repeat_number(nlist))