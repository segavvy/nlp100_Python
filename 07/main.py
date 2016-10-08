# coding: utf-8


def format_string(x, y, z):
	'''引数x, y, zを受け取り「x時のyはz」という文字列を返す

	引数:
	x, y, z -- 埋め込むパラメータ
	戻り値:
	整形した文字列
	'''
	return '{hour}時の{target}は{value}'.format(hour=x, target=y, value=z)


# テスト
x = 12
y = '気温'
z = 22.4
print(format_string(x, y, z))
