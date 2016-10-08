# coding: utf-8


def n_gram(target, n):
	'''指定されたリストからn-gramを作成

	引数:
	target -- 対象リスト
	n -- n-gramのn値（1ならuni-gram、2ならbi-gram...）
	戻り値:
	gramのリスト
	'''
	result = []
	for i in range(0, len(target) - n + 1):
		result.append(target[i:i + n])

	return result


target = 'I am an NLPer'
words_target = target.split(' ')

# 単語bi-gram
result = n_gram(words_target, 2)
print(result)

# 文字bi-gram
result = n_gram(target, 2)
print(result)

# 単語uni-gram
result = n_gram(words_target, 1)
print(result)

# 文字uni-gram
result = n_gram(target, 1)
print(result)

# 単語tri-gram
result = n_gram(words_target, 3)
print(result)

# 文字tri-gram
result = n_gram(target, 3)
print(result)
