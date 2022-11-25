words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

dict_words = {}

for i in words:
    unpack_words = list(i)
    unpack_words.sort()
    repack_words = ''
    for j in unpack_words:
        repack_words += j

# 6 ~ 10 번 라인을 
# t = ''.join(sorted(w)) 로 줄임

    if repack_words in dict_words:
        dict_words[repack_words].append(i)
    else:
        dict_words[repack_words] = [i]

print(dict_words)

d = {}
for w in words:
    t = ''.join(sorted(w))
    if t in d:
        d[t].append(w)
    else:
        d[t] = [t]
print(d)