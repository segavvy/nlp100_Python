# coding: utf-8
import pickle
from collections import OrderedDict
from scipy import io
import numpy as np

fname_dict_index_t = 'dict_index_t'
fname_matrix_x300 = 'matrix_x300'
fname_input = './wordsim353/combined.tab'
fname_output = 'combined_out.tab'


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

# 行列読み込み
matrix_x300 = io.loadmat(fname_matrix_x300)['matrix_x300']

# 評価データ読み込み
with open(fname_input, 'rt') as data_file, \
		open(fname_output, 'wt') as out_file:

	header = True
	for line in data_file:

		# 先頭行はスキップ
		if header is True:
			header = False
			continue

		cols = line.split('\t')

		try:
			# コサイン類似度算出
			dist = cos_sim(matrix_x300[dict_index_t[cols[0]]],
					matrix_x300[dict_index_t[cols[1]]])

		except KeyError:

			# 単語がなければコサイン類似度-1で出力
			dist = -1

		# 出力
		print('{}\t{}'.format(line.strip(), dist), file=out_file)
