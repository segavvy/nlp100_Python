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


# 集合の作成
set_x = set(n_gram('paraparaparadise', 2))
print('X:' + str(set_x))
set_y = set(n_gram('paragraph', 2))
print('Y:' + str(set_y))

# 和集合
set_or = set_x | set_y
print('和集合:' + str(set_or))

# 積集合
set_and = set_x & set_y
print('積集合:' + str(set_and))

# 差集合
set_sub = set_x - set_y
print('差集合:' + str(set_sub))

# 'se'が含まれるか？
print('seがXに含まれる:' + str('se' in set_x))
print('seがYに含まれる:' + str('se' in set_y))
