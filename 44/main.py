# coding: utf-8
import CaboCha
import re
import pydot_ng as pydot

fname = 'neko.txt.tmp'
fname_parsed = 'neko.txt.cabocha.tmp'


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


class Chunk:
	'''
	文節クラス
	形態素（Morphオブジェクト）のリスト（morphs）、係り先文節インデックス番号（dst）、
	係り元文節インデックス番号のリスト（srcs）をメンバー変数に持つ
	'''

	def __init__(self):
		'''初期化'''
		self.morphs = []
		self.srcs = []
		self.dst = -1

	def __str__(self):
		'''オブジェクトの文字列表現'''
		surface = ''
		for morph in self.morphs:
			surface += morph.surface
		return '{}\tsrcs{}\tdst[{}]'.format(surface, self.srcs, self.dst)

	def normalized_surface(self):
		'''句読点などの記号を除いた表層形'''
		result = ''
		for morph in self.morphs:
			if morph.pos != '記号':
				result += morph.surface
		return result

	def chk_pos(self, pos):
		'''指定した品詞（pos）を含むかチェックする

		戻り値：
		品詞（pos）を含む場合はTrue
		'''
		for morph in self.morphs:
			if morph.pos == pos:
				return True
		return False


def neco_lines():
	'''「吾輩は猫である」の係り受け解析結果のジェネレータ
	「吾輩は猫である」の係り受け解析結果を順次読み込んで、
	1文ずつChunkクラスのリストを返す

	戻り値：
	1文のChunkクラスのリスト
	'''
	with open(fname_parsed) as file_parsed:

		chunks = dict()		# idxをkeyにChunkを格納
		idx = -1

		for line in file_parsed:

			# 1文の終了判定
			if line == 'EOS\n':

				# Chunkのリストを返す
				if len(chunks) > 0:

					# chunksをkeyでソートし、valueのみ取り出し
					sorted_tuple = sorted(chunks.items(), key=lambda x: x[0])
					yield list(zip(*sorted_tuple))[1]
					chunks.clear()

				else:
					yield []

			# 先頭が*の行は係り受け解析結果なので、Chunkを作成
			elif line[0] == '*':

				# Chunkのインデックス番号と係り先のインデックス番号取得
				cols = line.split(' ')
				idx = int(cols[1])
				dst = int(re.search(r'(.*?)D', cols[2]).group(1))

				# Chunkを生成（なければ）し、係り先のインデックス番号セット
				if idx not in chunks:
					chunks[idx] = Chunk()
				chunks[idx].dst = dst

				# 係り先のChunkを生成（なければ）し、係り元インデックス番号追加
				if dst != -1:
					if dst not in chunks:
						chunks[dst] = Chunk()
					chunks[dst].srcs.append(idx)

			# それ以外の行は形態素解析結果なので、Morphを作りChunkに追加
			else:

				# 表層形はtab区切り、それ以外は','区切りでバラす
				cols = line.split('\t')
				res_cols = cols[1].split(',')

				# Morph作成、リストに追加
				chunks[idx].morphs.append(
					Morph(
						cols[0],		# surface
						res_cols[6],	# base
						res_cols[0],	# pos
						res_cols[1]		# pos1
					)
				)


def graph_from_edges_ex(edge_list, directed=False):
	'''pydot_ng.graph_from_edges()のノード識別子への対応版

	graph_from_edges()のedge_listで指定するタプルは
	識別子とグラフ表示時のラベルが同一のため、
	ラベルが同じだが実体が異なるノードを表現することができない。
	例えば文の係り受けをグラフにする際、文の中に同じ単語が
	複数出てくると、それらのノードが同一視されて接続されてしまう。

	この関数ではedge_listとして次の書式のタプルを受け取り、
	ラベルが同一でも識別子が異なるノードは別ものとして扱う。

	edge_list = [((識別子1,ラベル1),(識別子2,ラベル2)), ...]

	識別子はノードを識別するためのもので表示されない。
	ラベルは表示用で、同じでも識別子が異なれば別のノードになる。

	なお、オリジナルの関数にあるnode_prefixは未実装。

	戻り値：
	pydot.Dotオブジェクト
	'''

	if directed:
		graph = pydot.Dot(graph_type='digraph')

	else:
		graph = pydot.Dot(graph_type='graph')

	for edge in edge_list:

		id1 = str(edge[0][0])
		label1 = str(edge[0][1])
		id2 = str(edge[1][0])
		label2 = str(edge[1][1])

		# ノード追加
		graph.add_node(pydot.Node(id1, label=label1))
		graph.add_node(pydot.Node(id2, label=label2))

		# エッジ追加
		graph.add_edge(pydot.Edge(id1, id2))

	return graph


# 対象文字列を入力してもらい、そのままfnameに保存
with open(fname, mode='w') as out_file:
	out_file.write(input('文字列を入力してください--> '))

# 係り受け解析
parse_neko()

# 1文ずつリスト作成
for chunks in neco_lines():

	# 係り先があるものを列挙
	edges = []
	for i, chunk in enumerate(chunks):
		if chunk.dst != -1:

			# 記号を除いた表層形をチェック、空なら除外
			src = chunk.normalized_surface()
			dst = chunks[chunk.dst].normalized_surface()
			if src != '' and dst != '':
				edges.append(((i, src), (chunk.dst, dst)))

	# 描画
	if len(edges) > 0:
		graph = graph_from_edges_ex(edges, directed=True)
		graph.write_png('result.png')
