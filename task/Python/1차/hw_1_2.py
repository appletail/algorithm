score = {
'python': 80,
'django': 89,
'web': 83
}

score['algorithm'] = 90

score['python'] = 85

a = score.values()
b = sum(a) / len(score)
print(b)
