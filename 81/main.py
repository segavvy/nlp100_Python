# coding: utf-8
fname_input = 'corpus80.txt'
fname_output = 'corpus81.txt'
fname_countries = 'countries.txt'

# 国名一覧を読み込んで集合と辞書作成、ただし1語の国は含めない。
# 辞書には{ 最初の1語, [全体の語数1, 全体の語数2...] }を登録し、
# 全体の語数は降順でソートして格納する。
# たとえば最初の1語が'United'の国は次の6つある。
#	United States of America
#	United Mexican States
#   United Kingdom of Great Britain and Northern Ireland
#	United Arab Emirates
#   United Republic of Tanzania
#   United States
# この場合、全体の語数が4語、3語、8語、2語のものがあるので、
# 辞書には { 'United', [8, 4, 3, 2] } を登録する。
# 全体の個数を降順ソートするのは最長一致でマッチングさせるため。
set_country = set()
dict_country = {}
with open(fname_countries, 'rt') as data_file:
	for line in data_file:
		words = line.split(' ')
		if len(words) > 1:

			# 集合に追加
			set_country.add(line.strip())

			# 辞書に追加
			if words[0] in dict_country:
				lengths = dict_country[words[0]]
				if not len(words) in lengths:
					lengths.append(len(words))
					lengths.sort(reverse=True)
			else:
				dict_country[words[0]] = [len(words)]

# 1行ずつ処理
with open(fname_input, 'rt') as data_file, \
		open(fname_output, mode='wt') as out_file:
	for line in data_file:

		# 1語ずつチェック
		tokens = line.strip().split(' ')
		result = []		# 結果のトークン配列
		skip = 0		# >0なら複数語の続き
		for i in range(len(tokens)):

			# 複数語の続きの場合はスキップ
			if skip > 0:
				skip -= 1
				continue

			# 1語目が辞書にある？
			if tokens[i] in dict_country:

				# 後続の語数を切り取って集合にあるかチェック
				hit = False
				for length in dict_country[tokens[i]]:
					if ' '.join(tokens[i:i + length]) in set_country:

						# 複数語の国を発見したので'_'で連結して結果に追加
						result.append('_'.join(tokens[i:i + length]))
						skip = length - 1		# 残りの語はスキップ
						hit = True
						break
				if hit:
					continue

			# 複数語の国ではないので、そのまま結果に追加
			result.append(tokens[i])

		# 出力
		print(*result, sep=' ', end='\n', file=out_file)
