def is_user_data_valid(user_data):
    pass
    # 여기에 코드를 작성합니다.
    
    if user_data.get('id') or user_data.get('password') is False:
        return True         # 하나라도 비어있으면 False인게 사실이므로 True 반환
                            # 출력시 False로 됨
    else:
        return False        # 그 반대


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': '',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data1)) 
    # False 

    user_data2 = {
        'id': 'jungssafy',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data2)) 
    # True
