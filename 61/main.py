# coding: utf-8
import re
import leveldb

fname_db = 'test_db'

# keyをnameとidに分解するための正規表現
pattern = re.compile(r'''
    ^
    (.*)	# name
    \t      # 区切り
    (\d+)   # id
    $
    ''', re.VERBOSE + re.DOTALL)

# LevelDBオープン
db = leveldb.LevelDB(fname_db)

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

	# 活動場所のチェック、表示
	area = value.decode()
	if area != '':
		print('{}(id:{})の活動場所:{}'.format(name, id, area))
	else:
		print('{}(id:{})の活動場所は登録されていません'.format(name, id))
	hit = True

if not hit:
	print('{}は登録されていません'.format(clue))
