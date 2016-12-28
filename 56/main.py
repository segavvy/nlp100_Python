# coding: utf-8
import os
import subprocess
import xml.etree.ElementTree as ET

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


# nlp.txtを解析
parse_nlp()

# 解析結果のxmlをパース
root = ET.parse(fname_parsed)


# coreferenceの列挙し、代表参照表現に置き換える場所情報の辞書を作成
# 	辞書は{(sentence id, 開始token id), (終了token id, 代表参照表現)}...
rep_dict = {}
for coreference in root.iterfind('./document/coreference/coreference'):

	# 代表参照表現の取得
	rep_text = coreference.findtext('./mention[@representative="true"]/text')

	# 代表参照表現以外のmention列挙、辞書に追加
	for mention in coreference.iterfind('./mention'):
		if mention.get('representative', 'false') == 'false':

			# 必要な情報の抽出
			sent_id = int(mention.findtext('sentence'))
			start = int(mention.findtext('start'))
			end = int(mention.findtext('end'))

			# すでに辞書にある（＝開始位置は同じだが終わりが違う）場合は先勝ち
			if not (sent_id, start) in rep_dict:
				rep_dict[(sent_id, start)] = (end, rep_text)


# 本文をrep_dictで置き換えながら表示
for sentence in root.iterfind('./document/sentences/sentence'):
	sent_id = int(sentence.get('id'))		# sentenceのid
	org_rest = 0							# 置換中のtoken数の残り

	# token列挙
	for token in sentence.iterfind('./tokens/token'):
		token_id = int(token.get('id'))		# tokenのid

		# 置換対象？
		if org_rest == 0 and (sent_id, token_id) in rep_dict:

			# 辞書から終了位置と代表参照表現を取り出し
			(end, rep_text) = rep_dict[(sent_id, token_id)]

			# 代表参照表現＋カッコを挿入
			print('[' + rep_text + '] (', end='')
			org_rest = end - token_id		# 置換中のtoken数の残り

		# token出力
		print(token.findtext('word'), end='')

		# 置換の終わりなら閉じカッコを挿入
		if org_rest > 0:
			org_rest -= 1
			if org_rest == 0:
				print(')', end='')

		print(' ', end='')

	print()		# sentence単位で改行
