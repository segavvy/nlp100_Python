# coding: utf-8
import codecs
import snowballstemmer
import numpy as np

fname_sentiment = 'sentiment.txt'
fname_features = 'features.txt'
fname_result = 'result.txt'
fencoding = 'cp1252'		# Windows-1252らしい

division = 5			# データの分割数
learn_alpha = 6.0		# 学習レート
learn_count = 1000		# 学習の繰り返し数

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


def cost(data_x, theta, data_y):
	'''目的関数
	data_xに対して予測した結果と正解との差を算出

	戻り値：
	予測と正解との差
	'''
	m = data_y.size			# データ件数
	h = hypothesis(data_x, theta)		# data_yの予測値の行列
	j = 1 / m * np.sum(-data_y * np.log(h) -
			(np.ones(m) - data_y) * np.log(np.ones(m) - h))

	return j


def gradient(data_x, theta, data_y):
	'''最急降下における勾配の算出

	戻り値：
	thetaに対する勾配の行列
	'''
	m = data_y.size			# データ件数
	h = hypothesis(data_x, theta)		# data_yの予測値の行列
	grad = 1 / m * (h - data_y).dot(data_x)

	return grad


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


def create_training_set(sentiments, dict_features):
	'''正解データsentimentsから学習対象の行列と、極性ラベルの行列を作成
	学習対象の行例の大きさは正解データのレビュー数×(素性数+1)。
	列の値は、各レビューに対して該当素性がある場合は1、なければ0になる。
	列の素性のインデックスはdict_features['(素性)']で決まる。
	先頭の列は常に1で、素性に対応しない重みの学習用。
	dict_featuresに存在しない素性は無視。

	極性ラベルの行列の大きさはレビュー数×1。
	肯定的な内容が1、否定的な内容が0。

	戻り値：
	学習対象の行列,極性ラベルの行列
	'''

	# 行列を0で初期化
	data_x = np.zeros([len(sentiments), len(dict_features) + 1], dtype=np.float64)
	data_y = np.zeros(len(sentiments), dtype=np.float64)

	for i, line in enumerate(sentiments):

		# 素性抽出
		data_x[i] = extract_features(line[3:], dict_features)

		# 極性ラベル行列のセット
		if line[0:2] == '+1':
			data_y[i] = 1

	return data_x, data_y


def learn(data_x, data_y, alpha, count):
	'''ロジスティック回帰の学習

	戻り値：
	学習済みのtheta
	'''
	theta = np.zeros(data_x.shape[1])
	c = cost(data_x, theta, data_y)
	print('\t学習開始\tcost：{}'.format(c))

	for i in range(1, count + 1):

		grad = gradient(data_x, theta, data_y)
		theta -= alpha * grad

		# コストとthetaの最大調整量を算出して経過表示（100回に1回）
		if i % 100 == 0:
			c = cost(data_x, theta, data_y)
			e = np.max(np.absolute(alpha * grad))
			print('\t学習中(#{})\tcost：{}\tE:{}'.format(i, c, e))

	c = cost(data_x, theta, data_y)
	e = np.max(np.absolute(alpha * grad))
	print('\t学習完了(#{}) \tcost：{}\tE:{}'.format(i, c, e))
	return theta


def score(fname):
	'''結果ファイルからスコア算出
	fnameで指定された結果ファイルを読み込んで、正解率、適合率、再現率、F1スコアを返す

	戻り値：
	正解率,適合率,再現率,F1スコア
	'''
	# 結果を読み込んで集計
	TP = 0		# True-Positive		予想が+1、正解も+1
	FP = 0		# False-Positive	予想が+1、正解は-1
	FN = 0		# False-Negative	予想が-1、正解は+1
	TN = 0		# True-Negative		予想が-1、正解も-1

	with open(fname) as data_file:
		for line in data_file:
			cols = line.split('\t')

			if len(cols) < 3:
				continue

			if cols[0] == '+1':			# 正解
				if cols[1] == '+1':		# 予想
					TP += 1
				else:
					FN += 1
			else:
				if cols[1] == '+1':
					FP += 1
				else:
					TN += 1

	# 算出
	accuracy = (TP + TN) / (TP + FP + FN + TN)		# 正解率
	precision = TP / (TP + FP)		# 適合率
	recall = TP / (TP + FN)		# 再現率
	f1 = (2 * recall * precision) / (recall + precision) 	# F1スコア

	return accuracy, precision, recall, f1


# 素性辞書の読み込み
dict_features = load_dict_features()

# 正解データ読み込み
with codecs.open(fname_sentiment, 'r', fencoding) as file_in:
	sentiments_all = list(file_in)

# 正解データを5分割
sentiments = []
unit = int(len(sentiments_all) / division)		# 半端は未使用
for i in range(division):
	sentiments.append(sentiments_all[i * unit:(i + 1) * unit])


# 5分割交差検定
with open(fname_result, 'w') as file_out:
	for i in range(division):

		print('{}/{}'.format(i + 1, division))

		# 学習用と検証用に正解データを分割
		data_learn = []
		for j in range(division):
			if i == j:
				data_validation = sentiments[j]
			else:
				data_learn += sentiments[j]

		# 学習対象の配列と極性ラベルの配列作成
		data_x, data_y = create_training_set(data_learn, dict_features)

		# 学習
		theta = learn(data_x, data_y, alpha=learn_alpha, count=learn_count)

		# 検証
		for line in data_validation:

			# 素性抽出
			data_one_x = extract_features(line[3:], dict_features)

			# 予測、結果出力
			h = hypothesis(data_one_x, theta)
			if h > 0.5:
				file_out.write('{}\t{}\t{}\n'.format(line[0:2], '+1', h))
			else:
				file_out.write('{}\t{}\t{}\n'.format(line[0:2], '-1', 1 - h))

# 結果表示
print('\n学習レート：{}\t学習繰り返し数：{}'.format(learn_alpha, learn_count))
accuracy, precision, recall, f1 = score(fname_result)
print('正解率　\t{}\n適合率　\t{}\n再現率　\t{}\nF1スコア　\t{}'.format(
	accuracy, precision, recall, f1
))
