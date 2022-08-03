a = float(input())
b = float(input())
c = float(input())

d = (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
e = (-b - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)


f = round(d, 4)
g = round(e, 4)

print(f)
print(g)