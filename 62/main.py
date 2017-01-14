# coding: utf-8
import leveldb

fname_db = 'test_db'

# LevelDBオープン
db = leveldb.LevelDB(fname_db)

# valueが'Japan'のものを列挙
clue = 'Japan'.encode()
result = [value[0].decode() for value in db.RangeIter() if value[1] == clue]

# 件数表示
print('{}件'.format(len(result)))
