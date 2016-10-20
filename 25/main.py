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


# 基礎情報テンプレートの抽出条件のコンパイル
pattern = re.compile(r'''
	^\{\{基礎情報.*?$	# '{{基礎情報'で始まる行
	(.*?)		# キャプチャ対象、任意の0文字以上、非貪欲
	^\}\}$		# '}}'の行
	''', re.MULTILINE + re.VERBOSE + re.DOTALL)

# 基礎情報テンプレートの抽出
contents = pattern.findall(extract_UK())

# 抽出結果からのフィールド名と値の抽出条件コンパイル
pattern = re.compile(r'''
	^\|			# '|'で始まる行
	(.+?)		# キャプチャ対象（フィールド名）、任意の1文字以上、非貪欲
	\s*			# 空白文字0文字以上
	=
	\s*			# 空白文字0文字以上
	(.+?)		# キャプチャ対象（値）、任意の1文字以上、非貪欲
	(?:			# キャプチャ対象外のグループ開始
		(?=\n\|) 	# 改行+'|'の手前（肯定の先読み）
		| (?=\n$)	# または、改行+終端の手前（肯定の先読み）
	)			# グループ終了
	''', re.MULTILINE + re.VERBOSE + re.DOTALL)

# フィールド名と値の抽出
fields = pattern.findall(contents[0])

# 辞書にセット
result = {}
keys_test = []		# 確認用の出現順フィールド名リスト
for field in fields:
	result[field[0]] = field[1]
	keys_test.append(field[0])

# 確認のため表示（確認しやすいようにkeys_testを使ってフィールド名の出現順にソート）
for item in sorted(result.items(),
		key=lambda field: keys_test.index(field[0])):
	print(item)
