# coding: utf-8

fname_input = 'combined_out.tab'


class Data:
    def __init__(self, human_score, my_score):
        self.human_score = human_score
        self.my_score = my_score

    def __repr__(self):
        return 'Data%s' % repr(self.__dict__)

# データ配列作成
with open(fname_input) as data_file:
    def read_data():
        for line in data_file:
            word1, word2, human_score, my_score = line.split('\t')
            yield Data(float(human_score), float(my_score))
    data = list(read_data())

# 順位付け
data_sorted_by_human_score = sorted(data, key=lambda data: data.human_score)
for order, d in enumerate(data_sorted_by_human_score):
    d.human_order = order

data_sorted_by_my_score = sorted(data, key=lambda data: data.my_score)
for order, d in enumerate(data_sorted_by_my_score):
    d.my_order = order

# スピアマン相関係数算出
N = len(data)
total = sum((d.human_order - d.my_order) ** 2 for d in data)
result = 1 - (6 * total) / (N ** 3 - N)

print(result)
