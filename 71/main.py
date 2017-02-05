# coding: utf-8

# ストップワードのリスト	 http://xpo6.com/list-of-english-stop-words/ のCSV Formatより
stop_words = (
	'a,able,about,across,after,all,almost,also,am,among,an,and,any,are,'
	'as,at,be,because,been,but,by,can,cannot,could,dear,did,do,does,'
	'either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,'
	'him,his,how,however,i,if,in,into,is,it,its,just,least,let,like,'
	'likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,'
	'on,only,or,other,our,own,rather,said,say,says,she,should,since,so,'
	'some,than,that,the,their,them,then,there,these,they,this,tis,to,too,'
	'twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,'
	'will,with,would,yet,you,your').lower().split(',')


def is_stopword(str):
	'''文字がストップワードかどうかを返す
	大小文字は同一視する

	戻り値：
	ストップワードならTrue、違う場合はFalse
	'''
	return str.lower() in stop_words


# 正しく検出されることのテスト
assert is_stopword('a')				# リストの先頭
assert is_stopword('your')			# リストの末尾
assert is_stopword('often')			# リストの中間
assert is_stopword('on')			# リストの中間
assert is_stopword('A')				# 大小文字の同一視
assert is_stopword('Your')			# 大小文字の同一視
assert is_stopword('ofteN')			# 大小文字の同一視
assert is_stopword('ON')			# 大小文字の同一視

# 誤検出されないことのテスト
assert not is_stopword('0')			# リストにない
assert not is_stopword('z')			# リストにない
assert not is_stopword('bout')		# 後方一致されない
assert not is_stopword('acros')		# 前方一致されない
assert not is_stopword('fte')		# 中間一致されない
assert not is_stopword(' ')			# 空白
assert not is_stopword('\n')		# 制御コード
assert not is_stopword('')			# 空文字
