grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

price_lst = []
for i in grain_lst:
    price_lst.append(i[1])

maxprice = max(price_lst)

for i in grain_lst:
    if maxprice in i:
        print(i[0])

