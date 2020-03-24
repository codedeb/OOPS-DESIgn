#sorted Dictionaries

key = ['joh', 'lud', 'fred', 'wolf']
value = [65, 56,39,35]

composers = dict(zip(key, value ))

obj = sorted(composers.items(), key=lambda val: val[0])

print(obj)


