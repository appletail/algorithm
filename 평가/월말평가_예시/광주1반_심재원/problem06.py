def is_id_valid(user_data):
    pass
    # 여기에 코드를 작성합니다.

    # 가능한 모든 숫자 리스트
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
    
    # 리스트와 아이디 마지막 글자를 비교해 같으면 True 다르면 False 반환
    for i in num_list:
        if i == user_data.get('id')[-1]:
            return True
    
    return False


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False