steak = 50000
vat = 0.15

print(f"""스테이크   {format(steak, ',')}
+ VAT      {format(int(steak * vat), ',')}
총계 ₩    {format(int(steak + (steak * vat)), ',')}""")