# coding: utf-8
from scipy import sparse, io
import sklearn.decomposition

fname_matrix_x = 'matrix_x'
fname_matrix_x300 = 'matrix_x300'

# 行列読み込み
matrix_x = io.loadmat(fname_matrix_x)['matrix_x']

# 次元圧縮
clf = sklearn.decomposition.TruncatedSVD(300)
matrix_x300 = clf.fit_transform(matrix_x)
io.savemat(fname_matrix_x300, {'matrix_x300': matrix_x300})
