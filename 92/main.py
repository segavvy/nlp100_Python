# coding: utf-8
import pickle
from collections import OrderedDict
from scipy import io
import numpy as np

fname_dict_index_t = 'dict_index_t'
fname_matrix_x300 = 'matrix_x300'
fname_input = 'family.txt'
fname_output = 'family_out.txt'


def cos_sim(vec_a, vec_b):
	'''コサイン類似度の計算
	ベクトルvec_a、vec_bのコサイン類似度を求める

	戻り値：
	コサイン類似度
	'''
	norm_ab = np.linalg.norm(vec_a) * np.linalg.norm(vec_b)
	if norm_ab != 0:
		return np.dot(vec_a, vec_b) / norm_ab
	else:
		# ベクトルのノルムが0だと似ているかどうかの判断すらできないので最低値
		return -1


# 辞書読み込み
with open(fname_dict_index_t, 'rb') as data_file:
		dict_index_t = pickle.load(data_file)
keys = list(dict_index_t.keys())

# 行列読み込み
matrix_x300 = io.loadmat(fname_matrix_x300)['matrix_x300']

# 評価データ読み込み
with open(fname_input, 'rt') as data_file, \
		open(fname_output, 'wt') as out_file:

	for line in data_file:
		cols = line.split(' ')

		try:

			# ベクトル計算
			vec = matrix_x300[dict_index_t[cols[1]]] \
					- matrix_x300[dict_index_t[cols[0]]] \
					+ matrix_x300[dict_index_t[cols[2]]]

			# コサイン類似度の一番高い単語を抽出
			dist_max = -1
			index_max = 0
			result = ''
			for i in range(len(dict_index_t)):
				dist = cos_sim(vec, matrix_x300[i])
				if dist > dist_max:
					index_max = i
					dist_max = dist

			result = keys[index_max]

		except KeyError:

			# 単語がなければ0文字をコサイン類似度-1で出力
			result = ''
			dist_max = -1

		# 出力
		print('{} {} {}'.format(line.strip(), result, dist_max), file=out_file)
		print('{} {} {}'.format(line.strip(), result, dist_max))
