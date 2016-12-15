# coding: utf-8
import re

fname = 'nlp.txt'


def nlp_lines():
	'''nlp.txtを1文ずつ読み込むジェネレータ
	nlp.txtを順次読み込んで1文ずつ返す

	戻り値：
	1文の文字列
	'''
	with open(fname) as nlp_file:
		buf = ''		# 読み込みバッファ

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

		while True:

			# バッファが空なら読み込み
			if len(buf) < 1:

				buf = nlp_file.readline()
				if not buf:
					raise StopIteration		# ファイルの終端

				# 終端の改行除去
				buf = buf.rstrip('\n')
				if (len(buf) < 1):
					continue		# 空行はスキップ

			# バッファから1文を取得
			match = pattern.match(buf)
			if match:

				# 切り出した文を返す
				yield match.group(1)		# 先頭の文
				buf = match.group(2)		# 次の文以降

			else:

				# 区切りがないので、最後までが1文
				yield buf
				buf = ''


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
for word in nlp_words():
	print(word)
