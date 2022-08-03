string_s = input()

new_string = ''
new_string_I = ''

for s in string_s:
    if s.isalnum():
        new_string += s.lower()
    elif s == ' ':
        new_string += ' '
    elif s == ',':
        new_string += ','
    elif s == '.':
        new_string += '.'

new_string = new_string.replace('i', 'I', 1)

print(new_string)