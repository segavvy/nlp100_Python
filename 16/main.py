# coding: utf-8
import math

fname = 'hightemp.txt'
n = int(input('N--> '))

with open(fname) as data_file:
	lines = data_file.readlines()

count = len(lines)
unit = math.ceil(count / n)  # 1ファイル当たりの行数

for i, offset in enumerate(range(0, count, unit), 1):
	with open('child_{:02d}.txt'.format(i), mode='w') as out_file:
		for line in lines[offset:offset + unit]:
			out_file.write(line)
