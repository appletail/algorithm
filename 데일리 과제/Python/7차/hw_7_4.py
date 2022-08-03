def collatz(num):
    count = 0
    while count <= 500:
        if num % 2 == 0:
            num /= 2
            count += 1
        
        elif num == 1:
            return count

        elif num % 2 == 1:
            num = num * 3 + 1
            count += 1

    return -1

print(collatz(6))
print(collatz(512))
print(collatz(626331))
print(collatz(837799))