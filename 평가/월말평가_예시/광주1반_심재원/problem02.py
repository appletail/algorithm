def over(scores):
    pass
    # 여기에 코드를 작성합니다.
    over_sixty = []     # 60이 넘는 수를 저장하는 리스트

    for i in scores:                # 60이 넘으면 over_sixty에 저장
        if i >= 60:
            over_sixty.append(i)
    
    result = len(over_sixty)        # 리스트의 요소 갯수 계산

    return result



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(over(scores)) # 3
