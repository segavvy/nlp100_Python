# coding: utf-8
import pickle
from collections import OrderedDict
from scipy import io
import numpy as np
from sklearn.cluster import KMeans

fname_dict_index_t = 'dict_index_country'
fname_matrix_x300 = 'matrix_x300_country'

# 辞書読み込み
with open(fname_dict_index_t, 'rb') as data_file:
		dict_index_t = pickle.load(data_file)

# 行列読み込み
matrix_x300 = io.loadmat(fname_matrix_x300)['matrix_x300']

# KMeansクラスタリング
predicts = KMeans(n_clusters=5).fit_predict(matrix_x300)

# (国,分類番号)のリスト作成
result = zip(dict_index_t.keys(), predicts)

# 分類番号でソートして表示
for country, category in sorted(result, key=lambda x: x[1]):
	print('{}\t{}'.format(category, country))
