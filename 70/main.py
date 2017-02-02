# coding: utf-8
import codecs
import random

fname_pos = 'rt-polaritydata/rt-polarity.pos'
fname_neg = 'rt-polaritydata/rt-polarity.neg'
fname_smt = 'sentiment.txt'
fencoding = 'cp1252'		# Windows-1252らしい

result = []

# ポジティブデータの読み込み
with codecs.open(fname_pos, 'r', fencoding) as file_pos:
	result.extend(['+1 {}'.format(line.strip()) for line in file_pos])

# ネガティブデータの読み込み
with codecs.open(fname_neg, 'r', fencoding) as file_neg:
	result.extend(['-1 {}'.format(line.strip()) for line in file_neg])

# シャッフル
random.shuffle(result)

# 書き出し
with codecs.open(fname_smt, 'w', fencoding) as file_out:
	print(*result, sep='\n', file=file_out)

# 数の確認
cnt_pos = 0
cnt_neg = 0
with codecs.open(fname_smt, 'r', fencoding) as file_out:
	for line in file_out:
		if line.startswith('+1'):
			cnt_pos += 1
		elif line.startswith('-1'):
			cnt_neg += 1

print('pos:{}, neg:{}'.format(cnt_pos, cnt_neg))
