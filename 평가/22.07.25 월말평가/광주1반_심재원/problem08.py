# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def inventory_filter(item_type, inventory):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    result = []                               # 결과를 저장할 빈 리스트
    for data_i in inventory:                  # 인벤토리에 각 아이템들을 순환
        if data_i.get('type') == item_type:   # item_type과 딕셔너리내의 type과 일치하는지 확인
            result.append(data_i)             # 같으면 딕셔너리 전체를 리스트에 저장

    return result



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    item_type = 'weapon'
    inventory = [
        {
            'id': 1,
            'name': 'Elder Wand',
            'type': 'weapon',
            'grade': 'legend',
        },
        {
            'id': 2,
            'name': 'Healing Potion',
            'type': 'potion',
            'grade': 'normal',
        },
        {
            'id': 3,
            'name': 'Steel Helmet',
            'type': 'armor',
            'grade': 'rare',
        },
        {
            'id': 4,
            'name': 'Long Sword',
            'type': 'weapon',
            'grade': 'normal',
        },
    ]
    print(inventory_filter(item_type, inventory)) 
    # [{'id': 1, 'name': 'Elder Wand', 'type': 'weapon', 'grade': 'legend'}, {'id': 4, 'name': 'Long Sword', 'type': 'weapon', 'grade': 'normal'}]
