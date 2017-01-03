# coding: utf-8
import os
import subprocess
import xml.etree.ElementTree as ET
import pydot_ng as pydot

fname = 'nlp.txt'
fname_parsed = 'nlp.txt.xml'


def parse_nlp():
	'''nlp.txtをStanford Core NLPで解析しxmlファイルへ出力
	すでに結果ファイルが存在する場合は実行しない
	'''
	if not os.path.exists(fname_parsed):

		# StanfordCoreNLP実行、標準エラーはparse.outへ出力
		subprocess.run(
			'java -cp "/usr/local/lib/stanford-corenlp-full-2016-10-31/*"'
			' -Xmx2g'
			' edu.stanford.nlp.pipeline.StanfordCoreNLP'
			' -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref'
			' -file ' + fname + ' 2>parse.out',
			shell=True,		# shellで実行
			check=True		# エラーチェックあり
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


# nlp.txtを解析
parse_nlp()

# 解析結果のxmlをパース
root = ET.parse(fname_parsed)

# sentence列挙、1文ずつ処理
for sentence in root.iterfind('./document/sentences/sentence'):
	sent_id = int(sentence.get('id'))		# sentenceのid

	edges = []

	# dependencies列挙
	for dep in sentence.iterfind(
		'./dependencies[@type="collapsed-dependencies"]/dep'
	):

		# 句読点はスキップ
		if dep.get('type') != 'punct':

			# governor、dependent取得、edgesに追加
			govr = dep.find('./governor')
			dept = dep.find('./dependent')
			edges.append(
				((govr.get('idx'), govr.text), (dept.get('idx'), dept.text))
			)

	# 描画
	if len(edges) > 0:
		graph = graph_from_edges_ex(edges, directed=True)
		graph.write_png('{}.png'.format(sent_id))
