# coding: utf-8
fname_input = 'questions-words.txt'
fname_output = 'family.txt'

with open(fname_input, 'rt') as data_file, \
		open(fname_output, 'wt') as out_file:

	target = False		# 対象のデータ？
	for line in data_file:

		if target is True:

			# 対象データの場合は別のセクションになるまで出力
			if line.startswith(': '):
				break
			print(line.strip(), file=out_file)

		elif line.startswith(': family'):

			# 対象データ発見
			target = True
