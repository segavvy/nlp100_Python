# coding: utf-8
import pickle
from collections import OrderedDict
import numpy as np
from scipy import io
import word2vec

fname_input = 'corpus81.txt'
fname_word2vec_out = 'vectors.txt'
fname_dict_index_t = 'dict_index_t'
fname_matrix_x300 = 'matrix_x300'

# word2vecでベクトル化
#word2vec.word2vec(train=fname_input, output=fname_word2vec_out,
#	size=300, threads=4, binary=0)

# その結果を読み込んで行列と辞書作成
with open(fname_word2vec_out, 'rt') as data_file:

	# 先頭行から用語数と次元を取得
	work = data_file.readline().split(' ')
	size_dict = int(work[0])
	size_x = int(work[1])

	# 辞書と行列作成
	dict_index_t = OrderedDict()
	matrix_x = np.zeros([size_dict, size_x], dtype=np.float64)

	for i, line in enumerate(data_file):
		work = line.strip().split(' ')
		dict_index_t[work[0]] = i
		matrix_x[i] = work[1:]

# 結果の書き出し
io.savemat(fname_matrix_x300, {'matrix_x300': matrix_x})
with open(fname_dict_index_t, 'wb') as data_file:
	pickle.dump(dict_index_t, data_file)
