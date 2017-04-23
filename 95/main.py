# coding: utf-8
import numpy as np

fname_input = 'combined_out.tab'

with open(fname_input, 'rt') as data_file:

	# 類似度の配列作成
	human_score = []
	my_score = []
	N = 0

	for line in data_file:
		cols = line.split('\t')
		human_score.append(float(cols[2]))
		my_score.append(float(cols[3]))
		N += 1

# ソート
human_index_sorted = np.argsort(human_score)
my_index_sorted = np.argsort(my_score)

# 順位の配列作成
human_order = [0] * N
my_order = [0] * N
for i in range(N):
	human_order[human_index_sorted[i]] = i
	my_order[my_index_sorted[i]] = i

# スピアマン相関係数算出
total = 0
for i in range(N):
	total += pow(human_order[i] - my_order[i], 2)
result = 1 - (6 * total) / (pow(N, 3) - N)

print(result)
