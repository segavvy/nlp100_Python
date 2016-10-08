# coding: utf-8
target = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
result = []

words = target.split(' ')
for word in words:
	result.append(len(word) - word.count(',') - word.count('.'))

print(result)


