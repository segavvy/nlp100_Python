# coding: utf-8
import pickle
from collections import OrderedDict
from scipy import io
import numpy as np

fname_dict_index_t = 'dict_index_t'
fname_matrix_x300 = 'matrix_x300'

# 辞書読み込み
with open(fname_dict_index_t, 'rb') as data_file:
	dict_index_t = pickle.load(data_file)

# 行列読み込み
matrix_x300 = io.loadmat(fname_matrix_x300)['matrix_x300']

# 'United States'の単語ベクトル表示
print(matrix_x300[dict_index_t['United_States']])
