# coding: utf-8
import re
import snowballstemmer

fname = 'nlp.txt'


def nlp_lines():
	'''nlp.txtを1文ずつ読み込むジェネレータ
	nlp.txtを順次読み込んで1文ずつ返す

	戻り値：
	1文の文字列
	'''
	with open(fname) as lines:

		# 文切り出しの正規表現コンパイル
		pattern = re.compile(r'''
			(
				^					# 行頭
				.*?					# 任意のn文字、最少マッチ
				[\.|\;|\:|\?|\!]	# . or ; or : or ? or !
			)
			\s						# 空白文字
			(
				[A-Z].*				# 英大文字以降（＝次の文以降)

			)
		''', re.MULTILINE + re.VERBOSE + re.DOTALL)

		for line in lines:

			line = line.strip()		# 前後の空白文字除去
			while len(line) > 0:

				# 行から1文を取得
				match = pattern.match(line)
				if match:

					# 切り出した文を返す
					yield match.group(1)		# 先頭の文
					line = match.group(2)		# 次の文以降

				else:

					# 区切りがないので、最後までが1文
					yield line
					line = ''


def nlp_words():
	'''nlp.txtを1単語ずつ返すジェネレータ
	文の終わりでは空文字を返す。

	戻り値：
	1単語、ただし文の終わりでは空文字を返す
	'''
	for line in nlp_lines():

		# 単語に分解、終端の区切り文字は除去して返す
		for word in line.split(' '):
			yield word.rstrip('.,;:?!')

		# 文の終わりは空文字
		yield ''


# 読み込み
stemmer = snowballstemmer.stemmer('english')
for word in nlp_words():

	# 元の結果とステミング結果を出力
	print('{}\t{}'.format(word, stemmer.stemWord(word)))
