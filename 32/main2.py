# coding: utf-8
import MeCab
fname = 'neko.txt'
fname_parsed = 'neko.txt.mecab'


def parse_neko():
	'''「吾輩は猫である」を形態素解析
	「吾輩は猫である」(neko.txt)を形態素解析してneko.txt.mecabに保存する
	'''

	with open(fname) as data_file, \
			open(fname_parsed, mode='w') as out_file:

		mecab = MeCab.Tagger()
		out_file.write(mecab.parse(data_file.read()))


def neco_lines():
	'''「吾輩は猫である」の形態素解析結果のジェネレータ
	「吾輩は猫である」の形態素解析結果を順次読み込んで、各形態素を
	・表層形（surface）
	・基本形（base）
	・品詞（pos）
	・品詞細分類1（pos1）
	の4つをキーとする辞書に格納し、1文ずつ、この辞書のリストとして返す

	戻り値：
	1文の各形態素を辞書化したリスト
	'''
	with open(fname_parsed) as file_parsed:

		morphemes = []
		for line in file_parsed:

			# 表層形はtab区切り、それ以外は','区切りでバラす
			cols = line.split('\t')
			if(len(cols) < 2):
				raise StopIteration		# 区切りがなければ終了
			res_cols = cols[1].split(',')

			# 辞書作成、リストに追加
			morpheme = {
				'surface': cols[0],
				'base': res_cols[6],
				'pos': res_cols[0],
				'pos1': res_cols[1]
			}
			morphemes.append(morpheme)

			# 品詞細分類1が'句点'なら文の終わりと判定
			if res_cols[1] == '句点':
				yield morphemes
				morphemes = []


# 形態素解析
parse_neko()

# 1文ずつ辞書のリストを取得し動詞を抽出
list_verbs = []		# 出現順リスト、重複あり
for line in neco_lines():
	list_verbs.extend(
		morpheme['base'] for morpheme in line if morpheme['pos'] == '動詞'
	)
verbs = set(list_verbs)

# 確認しやすいようlist_verbsを使って出現順にソートして表示
print(sorted(verbs, key=list_verbs.index))
