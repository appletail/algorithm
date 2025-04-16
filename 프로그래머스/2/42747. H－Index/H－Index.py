def solution(citations):
    citations.sort(reverse=True)  # 내림차순 정렬
    h_index = 0

    for i, citation in enumerate(citations):
        if citation >= i + 1:
            h_index = i + 1
        else:
            break
    return h_index