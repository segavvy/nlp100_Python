# coding: utf-8
import codecs
import numpy as np

fname_features = 'features.txt'
fname_theta = 'theta.npy'
fencoding = 'cp1252'		# Windows-1252らしい

# 素性読み込み
with codecs.open(fname_features, 'r', fencoding) as file_in:
	features = list(file_in)

# 学習結果の読み込み
theta = np.load(fname_theta)

# 重みでソートしてインデックス配列作成
index_sorted = np.argsort(theta)

# 上位、下位10件表示
print('top 10')
for index in index_sorted[:-11:-1]:
	print('\t{}\t{}'.format(theta[index],
			features[index - 1].strip() if index > 0 else '(none)'))

print('worst 10')
for index in index_sorted[0:10:]:
	print('\t{}\t{}'.format(theta[index],
			features[index - 1].strip() if index > 0 else '(none)'))
