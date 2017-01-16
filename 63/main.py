# coding: utf-8
import gzip
import json
import re
import leveldb

fname = 'artist.json.gz'
fname_db = 'test_db'

# keyをnameとidに分解するための正規表現
pattern = re.compile(r'''
    ^
    (.*)	# name
    \t		# 区切り
    (\d+)	# id
    $
    ''', re.VERBOSE + re.DOTALL)

# LevelDBオープン、ない時だけ作成
try:
	db = leveldb.LevelDB(fname_db, error_if_exists=True)

	# gzファイル読み込み、パース
	with gzip.open(fname, 'rt') as data_file:
		for line in data_file:
			data_json = json.loads(line)

			# name+idとtagsをDBへ追加
			key = data_json['name'] + '\t' + str(data_json['id'])
			value = data_json.get('tags')		# tagsはないことがあるのでチェック
			if value is None:
				value = []
			db.Put(key.encode(), json.dumps(value).encode())

	# 確認のため登録件数を表示
	print('{}件登録しました。'.format(len(list(db.RangeIter(include_value=False)))))

except:
	db = leveldb.LevelDB(fname_db)
	print('既存のDBを使います。')

# 条件入力
clue = input('アーティスト名を入力してください--> ')
hit = False

# アーティスト名+'\t'で検索
for key, value in db.RangeIter(key_from=(clue + '\t').encode()):

	# keyをnameとidに戻す
	match = pattern.match(key.decode())
	name = match.group(1)
	id = match.group(2)

	# 異なるアーティストになったら終了
	if name != clue:
		break

	# タグ情報取得
	tags = json.loads(value.decode())
	print('{}(id:{})のタグ情報:'.format(name, id))
	if len(tags) > 0:
		for tag in tags:
			print('\t{}({})'.format(tag['value'], tag['count']))
	else:
		print('\tタグはありません')
	hit = True

if not hit:
	print('{}は登録されていません'.format(clue))
