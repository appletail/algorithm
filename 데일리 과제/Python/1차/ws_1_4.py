a = list(range(1, 1000))
b = a[1: 1000: 2]
c = a[6: 1000: 7]

d = b + c
d = set(d)
e = sum(d)

print(e)
