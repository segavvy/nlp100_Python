# coding: utf-8
import codecs
import snowballstemmer
import numpy as np

fname_sentiment = 'sentiment.txt'
fname_features = 'features.txt'
fname_theta = 'theta.npy'
fname_result = 'result.txt'
fencoding = 'cp1252'		# Windows-1252らしい

stemmer = snowballstemmer.stemmer('english')

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


def hypothesis(data_x, theta):
	'''仮説関数
	data_xに対して、thetaを使ってdata_yを予測

	戻り値：
	予測値の行列
	'''
	return 1.0 / (1.0 + np.exp(-data_x.dot(theta)))


def extract_features(data, dict_features):
	'''文章から素性を抽出
	文章からdict_featuresに含まれる素性を抽出し、
	dict_features['(素性)']の位置を1にした行列を返す。
	なお、先頭要素は固定で1。素性に対応しない重み用。

	戻り値：
	先頭要素と、該当素性の位置+1を1にした行列
	'''
	data_one_x = np.zeros(len(dict_features) + 1, dtype=np.float64)
	data_one_x[0] = 1		# 先頭要素は固定で1、素性に対応しない重み用。

	for word in data.split(' '):

		# 前後の空白文字除去
		word = word.strip()

		# ストップワード除去
		if is_stopword(word):
			continue

		# ステミング
		word = stemmer.stemWord(word)

		# 素性のインデックス取得、行列の該当箇所を1に
		try:
			data_one_x[dict_features[word]] = 1
		except:
			pass		# dict_featuresにない素性は無視

	return data_one_x


def load_dict_features():
	'''features.txtを読み込み、素性をインデックスに変換するための辞書を作成
	インデックスの値は1ベースで、features.txtにおける行番号と一致する。

	戻り値：
	素性をインデックスに変換する辞書
	'''
	with codecs.open(fname_features, 'r', fencoding) as file_in:
		return {line.strip(): i for i, line in enumerate(file_in, start=1)}


# 素性辞書の読み込み
dict_features = load_dict_features()

# 学習結果の読み込み
theta = np.load(fname_theta)

# 学習データを読み込んで予測
with codecs.open(fname_sentiment, 'r', fencoding) as file_in, \
		open(fname_result, 'w') as file_out:

	for line in file_in:

		# 素性抽出
		data_one_x = extract_features(line[3:], dict_features)

		# 予測、結果出力
		h = hypothesis(data_one_x, theta)
		if h > 0.5:
			file_out.write('{}\t{}\t{}\n'.format(line[0:2], '+1', h))
		else:
			file_out.write('{}\t{}\t{}\n'.format(line[0:2], '-1', 1 - h))
