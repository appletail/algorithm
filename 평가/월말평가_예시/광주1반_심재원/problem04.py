def turn(temperatures):
    pass
    # 여기에 코드를 작성합니다.

    maximin = {}
    maximum = []
    minimum = []

    for maxV in temperatures:       # 각각의 값을 리스트에 추가
        maximum.append(maxV[0])
        minimum.append(maxV[1])
    
    maximin['maximum'] = maximum    # 리스트를 딕셔너리에 추가
    maximin['minimum'] = minimum

    return maximin                  # 딕셔너리 반환


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperatures = [
        [9, 3],
        [9, 0],
        [11, -3],
        [11, 1],
        [8, -3],
        [7, -3],
        [-4, -12]
    ]
    print(turn(temperatures)) 
    # {
    #     'maximum': [9, 9, 11, 11, 8, 7, -4], 
    #     'minimum': [3, 0, -3, 1, -3, -3, -12]
    # }

