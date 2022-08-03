munja = input()
munja_len = len(munja) // 2

if len(munja) % 2:
    print(munja[munja_len])
else:
    print(munja[munja_len - 1: munja_len +1])