n = int(input())
m = int(input())
if m:
    broken = input().split()
else:
    broken = []

a = -1
b = abs(100 - n)
while a <= 1000000:
    a += 1
    if b <= len(str(a)) + abs(n - a):
        continue
    for i in str(a):
        if i in broken:
            break
    else:
        b = min(b, len(str(a)) + abs(n - a))


print(b)
