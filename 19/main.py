# coding: utf-8
from itertools import groupby
fname = 'hightemp.txt'

# 都道府県名の読み込み
lines = open(fname).readlines()
kens = [line.split('\t')[0] for line in lines]

# 都道府県で集計し、(都道府県, 出現頻度)のリスト作成
kens.sort()    # goupbyはソート済みが前提
result = [(ken, len(list(group))) for ken, group in groupby(kens)]

# 出現頻度でソート
result.sort(key=lambda ken: ken[1], reverse=True)

# 結果出力
for ken in result:
	print('{ken}({count})'.format(ken=ken[0], count=ken[1]))
