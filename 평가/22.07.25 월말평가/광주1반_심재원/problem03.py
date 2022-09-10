# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def get_user_id(data):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.

    result = str(data.get('id'))        # id의 문자열을 str로 확실히 변환

    return f"'{result}'"                # f스트링을 이용해 '문자열'형식으로 변환


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    user_data = {
        "id": "jungssafy",
        "password": "q1w2e3r4",
        "password_confirm": "q1w2e3r4"
    }
    print(get_user_id(user_data)) # 'jungssafy'
