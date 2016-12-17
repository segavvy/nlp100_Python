# coding: utf-8
import re

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


# 読み込み
for line in nlp_lines():
	print(line)
