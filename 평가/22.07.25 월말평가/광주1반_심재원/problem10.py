# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def get_final_position(N, mat, moves):
    pass
    # 1. 내 위치를 찾음
    # 2. 찾은 위치에서 이동
    # 3. 이동한 값이 범위를 벗어나는지 확인
    # 4. 안벗어나면 캐릭터 좌표값 반환
    # 5. 벗어나면 None 반환

    line_num = -1             # 행을 0부터 시작하기 위한 값

    for line in mat:          # 행 값 구하는 for
        line_num += 1
        ver_num = -1

        for ver in line:      # 열 값 구하는 for
            ver_num += 1
            if ver == 1:
                x, y = line_num, ver_num   # 위치를 구하면 좌표값 입력


    for M in moves:           # x, y 좌표값 이동
        if M == 0:          
            x -= 1
        elif M == 1:
            x += 1
        elif M == 2:
            y -= 1
        elif M == 3:
            y += 1
    
    if 0 <= x < N and 0 <= y < N:   # 구역 제한
        return [x, y]               # 범위를 안벗어난 경우
    else:
        return                      # 범위를 벗어난 경우



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    N = 3
    mat = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ] 
    moves1 = [1, 1, 3]
    print(get_final_position(N, mat, moves1)) # [2, 1]
    
    moves2 = [1, 3, 3]
    print(get_final_position(N, mat, moves2)) # [1, 2]