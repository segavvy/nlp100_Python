# coding: utf-8

fname_result = 'result.txt'


def score(fname):
	'''結果ファイルからスコア算出
	結果ファイルを読み込んで、正解率、適合率、再現率、F1スコアを返す

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


# スコア算出
accuracy, precision, recall, f1 = score(fname_result)
print('正解率　\t{}\n適合率　\t{}\n再現率　\t{}\nF1スコア　\t{}'.format(
	accuracy, precision, recall, f1
))
