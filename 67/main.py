# coding: utf-8
import json
from pymongo import MongoClient
from bson.objectid import ObjectId


def support_ObjectId(obj):
	'''json.dumps()でObjectIdを処理するための関数
	ObjectIdはjsonエンコードできない型なので、文字列型に変換する

	戻り値：
	ObjectIdから変換した文字列
	'''
	if isinstance(obj, ObjectId):
		return str(obj)		# 文字列として扱う
	raise TypeError(repr(obj) + " is not JSON serializable")


# MongoDBのデータベースtestdbにコレクションartistにアクセス
client = MongoClient()
db = client.testdb
collection = db.artist

# 条件入力
clue = input('アーティストの別名を入力してください--> ')

# 検索
for i, doc in enumerate(collection.find({'aliases.name': clue}), start=1):

	# 整形して表示
	print('{}件目の内容：\n{}'.format(i,
		json.dumps(
			doc, indent='\t', ensure_ascii=False,
			sort_keys=True, default=support_ObjectId
		)
	))
