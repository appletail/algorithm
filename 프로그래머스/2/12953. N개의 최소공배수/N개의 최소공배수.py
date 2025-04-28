def solution(arr):
    maxNum = max(arr)
    multiple = 1
    while True:
        tmp = maxNum * multiple
        multiple += 1
        for num in arr:
            if tmp % num:
                break
        else:
            return tmp
