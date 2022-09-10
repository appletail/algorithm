# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    x, y = position     # 위치를 x, y 값에 대입
    if M == 0:          # M에 따른 위치값 변화
        x -= 1
    elif M == 1:
        x += 1
    elif M == 2:
        y -= 1
    elif M == 3:
        y += 1


    if 0 <= x < N and 0 <= y < N:   # 구역 제한
        return True                 # 범위를 안벗어난 경우
    else:
        return False                # 범위를 벗어난 경우
    
    



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0))) # True
    print(is_position_safe(3, 0, (0, 0))) # False
