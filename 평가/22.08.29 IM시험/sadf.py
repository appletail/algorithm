def my_sort(arr):
    for i in range(N):
        min_index = i
        for j in range(i+1, N):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def my_max(lst):
    max_V = 0
    for i in range(len(lst)):
        if lst[i] > max_V:
            max_V = lst[i]
    return max_V

def my_min(lst):
    min_V = 100
    for i in range(len(lst)):
        if lst[i] < min_V:
            min_V = lst[i]
    return min_V

T = int(input())
for tc in range(1, T+1):
    N, Kmin, Kmax = map(int, input().split())
    arr = list(map(int, input().split()))

    my_sort(arr)
    lst = set(arr)

    A_result = []
    B_result = []
    C_result = []
    for i in lst:
        for j in lst:
            A = []
            B = []
            C = []

            if i < j:
                T1 = i
                T2 = j
                for z in range(N):
                    if arr[z] >= T2:
                        A.append(arr[z])
                    elif T1 <= arr[z] < T2:
                        B.append(arr[z])
                    else:
                        C.append(arr[z])

                if len(A) > Kmax or len(B) > Kmax or len(C) > Kmax:
                    pass
                elif len(A) < Kmin or len(B) < Kmin or len(C) < Kmin:
                    pass
                else:
                    A_result.append(len(A))
                    B_result.append(len(B))
                    C_result.append(len(C))
            else:
                pass

    if len(A_result) == 0 and len(B_result) == 0 and len(C_result) == 0:
        print(f'#{tc}', int(-1))
    else:
        SCORE_RES = 100
        for i in range(len(A_result)):
            score_result = []
            score_result.append(A_result[i])
            score_result.append(B_result[i])
            score_result.append(C_result[i])
            MAX = my_max(score_result)
            MIN = my_min(score_result)
            s = MAX - MIN
            if SCORE_RES > s:
                SCORE_RES = s
        print(f'#{tc} {SCORE_RES}')