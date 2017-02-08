# coding: utf-8
import codecs
import snowballstemmer
from collections import Counter

fname_sentiment = 'sentiment.txt'
fname_features = 'features.txt'
fencoding = 'cp1252'		# Windows-1252らしい

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


# 素性抽出
stemmer = snowballstemmer.stemmer('english')
word_counter = Counter()

with codecs.open(fname_sentiment, 'r', fencoding) as file_in:
	for line in file_in:
		for word in line[3:].split(' '):		# line[3:]で極性ラベル除去

			# 前後の空白文字除去
			word = word.strip()

			# ストップワード除去
			if is_stopword(word):
				continue

			# ステミング
			word = stemmer.stemWord(word)

			# '!'と'?'を除く1文字以下は除外
			if word != '!' and word != '?' and len(word) <= 1:
				continue

			# 候補に追加
			word_counter.update([word])

# 出現数が6以上のものを採用
features = [word for word, count in word_counter.items() if count >= 6]

# 書き出し
with codecs.open(fname_features, 'w', fencoding) as file_out:
	print(*features, sep='\n', file=file_out)
