def fee(time, km):
    result = 0

    # 대여 요금
    result += (time / 10) * 1200

    # 보험료
    if time % 60 == 50:
        result += ((time // 30) + 1) * 525
    else:
        result += time // 30 * 525

    # 주행요금
    if km > 100:
        result += 100 * 170 + ((km - 100) * 85)
    else:
        result += km * 170

    return print(int(result))


fee(660, 110)