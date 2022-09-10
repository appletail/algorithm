# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    result = ''

    for w in word:                          # 문자열의 글자 하나하나씩 처리
        num = ord(w)                        # 문자를 코드로 변환
        num += n                            # n만큼 덧셈
        if w.isupper() and num > 90:        # 대문자이고 90을 초과하면
            num -= 26                       # 26을 빼줌
        elif w.islower() and num > 122:     # 소문자이고 122를 초과하면
            num -= 26                       # 26을 빼줌
        num = chr(num)                      # 글자로 바꾼 뒤 반환
        result += num
    return result


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # fuuqj
    print(caesar('ssafy', 1))
    # ttbgz
    print(caesar('Python', 10))
    # Zidryx