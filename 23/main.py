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
	^		# 行頭
	(={2,})	# キャプチャ対象、2個以上の'='
	\s*		# 余分な0個以上の空白（'哲学'や'婚姻'の前後に余分な空白があるので除去）
	(.+?)	# キャプチャ対象、任意の文字が1文字以上、非貪欲（以降の条件の巻き込み防止）
	\s*		# 余分な0個以上の空白
	\1		# 後方参照、1番目のキャプチャ対象と同じ内容
	.*		# 任意の文字が0文字以上
	$		# 行末
	''', re.MULTILINE + re.VERBOSE)

# 抽出
result = pattern.findall(extract_UK())

# 結果表示
for line in result:
	level = len(line[0]) - 1    # '='の数-1
	print('{indent}{sect}({level})'.format(
		indent='\t' * (level - 1), sect=line[1], level=level))
