# coding: utf-8
import pickle
from collections import OrderedDict
from scipy import io
import numpy as np

from scipy.cluster.hierarchy import ward, dendrogram
from matplotlib import pyplot as plt

fname_dict_index_t = 'dict_index_country'
fname_matrix_x300 = 'matrix_x300_country'


# 辞書読み込み
with open(fname_dict_index_t, 'rb') as data_file:
		dict_index_t = pickle.load(data_file)

# 行列読み込み
matrix_x300 = io.loadmat(fname_matrix_x300)['matrix_x300']

# Ward法でクラスタリング
ward = ward(matrix_x300)
print(ward)

# デンドログラム表示
dendrogram(ward, labels=list(dict_index_t.keys()), leaf_font_size=8)
plt.show()
