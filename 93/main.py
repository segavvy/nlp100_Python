# coding: utf-8
fname_input = 'family_out.txt'

with open(fname_input, 'rt') as data_file:

	# 1行ずつチェック
	correct = 0
	total = 0

	for line in data_file:
		cols = line.split(' ')
		total += 1
		if cols[3] == cols[4]:
			correct += 1

# 正解率表示
print('{} ({}/{})'.format(correct / total, correct, total))
