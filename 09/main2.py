# coding: utf-8
import random


def Typoglycemia(target):
	'''タイポグリセミア【日本語バージョン】
	スペースで区切られた単語列に対して、各単語の先頭と末尾の文字は残し、
	それ以外の文字の順序をランダムに並び替える。
	ただし、【長さが3以下】の単語は並び替えない。

	引数:
	target -- 対象の文字列
	戻り値:
	変換した文字列
	'''
	result = []
	for word in target.split(' '):
		if len(word) <= 3:
			result.append(word)
		else:
			chr_list = list(word[1:-1])
			random.shuffle(chr_list)
			result.append(word[0] + ''.join(chr_list) + word[-1])

	return ' '.join(result)

# 対象文字列の入力
target = input('文字列を入力してください--> ')

# タイポグリセミア
result = Typoglycemia(target)
print('変換結果:' + result)
