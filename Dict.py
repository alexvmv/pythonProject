dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}

dict2 = {}

for key, val in dict.items():
    if val >= 3:
        dict2.update({key: val})

print(dict2)
