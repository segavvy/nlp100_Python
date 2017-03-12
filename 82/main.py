# coding: utf-8
import random
fname_input = 'corpus81.txt'
fname_output = 'context.txt'

# 1行ずつ処理
with open(fname_input, 'rt') as data_file, \
		open(fname_output, mode='wt') as out_file:
	for i, line in enumerate(data_file):

		# 1語ずつ処理
		tokens = line.strip().split(' ')
		for j in range(len(tokens)):

			t = tokens[j]					# 単語t
			d = random.randint(1, 5)		# 文脈幅d

			# 前後d語以内の語の列挙
			for k in range(max(j - d, 0), min(j + d + 1, len(tokens))):
				if j != k:
					print('{}\t{}'.format(t, tokens[k]), file=out_file)

		# 経過表示
		if i % 10000 == 0:
			print('{} done.'.format(i))
