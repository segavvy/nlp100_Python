# coding: utf-8
import gzip
import json
import leveldb

fname = 'artist.json.gz'
fname_db = 'test_db'

# LevelDBオープン、なければ作成
db = leveldb.LevelDB(fname_db)

# gzファイル読み込み、パース
with gzip.open(fname, 'rt') as data_file:
	for line in data_file:
		data_json = json.loads(line)

		# key=name+id、value=areaとしてDBへ追加
		key = data_json['name'] + '\t' + str(data_json['id'])
		value = data_json.get('area')		# areaはないことがあるのでチェック
		if value is None:
			value = ''
		db.Put(key.encode(), value.encode())

# 確認のため登録件数を表示
print('{}件登録しました。'.format(len(list(db.RangeIter(include_value=False)))))
