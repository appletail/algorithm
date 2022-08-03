def count_vowels(stri):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = 0
    for vowel in vowels:
        result += stri.count(vowel)
    
    return print(result)

count_vowels('apple') #=> 2
count_vowels('banana') #=> 3
