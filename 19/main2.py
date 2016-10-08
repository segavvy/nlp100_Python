# coding: utf-8
from itertools import groupby
fname = 'hightemp.txt'


def get_ken(target):
	'''1行分のデータから都道府県部分を切り出す

	引数：
	target -- 1行分のデータ
	戻り値：
	都道府県の文字列
	'''
	return target.split('\t')[0]

# 読み込み
lines = open(fname).readlines()

# 都道府県で集計
lines.sort(key=get_ken)    # goupbyはソート済みが前提
groups = groupby(lines, key=get_ken)

# 集計結果を(都道府県, 出現頻度, 該当行のリスト)のリストに変換
result = []
for ken, group in groups:
	lines = list(group)
	result.append((ken, len(lines), lines))

# 出現頻度でソート
result.sort(key=lambda group: group[1], reverse=True)

# 結果表示
for group in result:
	for line in group[2]:
		print(line, end='')
