veg = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
veg_price = []

for i in range(len(veg)):
    veg_price.append(veg[i][1])

veg_hi = max(veg_price)
veg_hiindex = veg_price.index(veg_hi)

veg_hiname = veg[veg_hiindex][0]

print(veg_hiname)