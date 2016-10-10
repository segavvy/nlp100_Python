# coding: utf-8
import gzip
import json
import re
fname = 'jawiki-country.json.gz'


def extract_UK():
	'''イギリスに関する記事本文を取得

	戻り値：
	イギリスの記事本文
	'''

	with gzip.open(fname, 'rt') as data_file:
		for line in data_file:
			data_json = json.loads(line)
			if data_json['title'] == 'イギリス':
				return data_json['text']

	raise ValueError('イギリスの記事が見つからない')


# 正規表現のコンパイル
pattern = re.compile(r'''
	^	# 行頭
	(	# キャプチャ対象のグループ開始
	.*	# 任意の文字0文字以上
	\[\[Category:
	.*	# 任意の文字0文字以上
	\]\]
	.*	# 任意の文字0文字以上
	)	# グループ終了
	$	# 行末
	''', re.MULTILINE + re.VERBOSE)

# 抽出
result = pattern.findall(extract_UK())

# 結果表示
for line in result:
	print(line)
