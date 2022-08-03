def group_anagrams(words):
    dic = {}
    result = []
    for word in words:
        s_w = sorted(word)
        sorted_word = ''
        
        for s in s_w:
            sorted_word += s

        if sorted_word not in dic:
            dic[sorted_word] = [word]
        else:
            dic[sorted_word].append(word)
    
    dic = list(dic.items())
    for i in dic:
        result.append(i[1])
    
    return print(result)


words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
group_anagrams(words)
