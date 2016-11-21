# coding: utf-8
import CaboCha

fname = 'neko.txt'
fname_parsed = 'neko.txt.cabocha'


def parse_neko():
	'''「吾輩は猫である」を係り受け解析
	「吾輩は猫である」(neko.txt)を係り受け解析してneko.txt.cabochaに保存する
	'''
	with open(fname) as data_file, \
			open(fname_parsed, mode='w') as out_file:

		cabocha = CaboCha.Parser()
		for line in data_file:
			out_file.write(
				cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE)
			)


class Morph:
	'''
	形態素クラス
	表層形（surface）、基本形（base）、品詞（pos）、品詞細分類1（pos1）を
	メンバー変数に持つ
	'''
	def __init__(self, surface, base, pos, pos1):
		'''初期化'''
		self.surface = surface
		self.base = base
		self.pos = pos
		self.pos1 = pos1

	def __str__(self):
		'''オブジェクトの文字列表現'''
		return 'surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'\
			.format(self.surface, self.base, self.pos, self.pos1)


def neco_lines():
	'''「吾輩は猫である」の係り受け解析結果のジェネレータ
	「吾輩は猫である」の係り受け解析結果を順次読み込んで、
	1文ずつMorphクラスのリストを返す

	戻り値：
	1文のMorphクラスのリスト
	'''
	with open(fname_parsed) as file_parsed:

		morphs = []
		for line in file_parsed:

			# 1文の終了判定
			if line == 'EOS\n':
				yield morphs
				morphs = []

			else:
				# 先頭が*の行は係り受け解析結果なのでスキップ
				if line[0] == '*':
					continue

				# 表層形はtab区切り、それ以外は','区切りでバラす
				cols = line.split('\t')
				res_cols = cols[1].split(',')

				# Morph作成、リストに追加
				morphs.append(Morph(
					cols[0],		# surface
					res_cols[6],	# base
					res_cols[0],	# pos
					res_cols[1]		# pos1
				))

		raise StopIteration


# 係り受け解析
parse_neko()

# 1文ずつリスト作成
for i, morphs in enumerate(neco_lines(), 1):

	# 3文目を表示
	if i == 3:
		for morph in morphs:
			print(morph)
		break
