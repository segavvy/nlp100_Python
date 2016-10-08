# coding: utf-8

fname = 'hightemp.txt'
lines = open(fname).readlines()
lines.sort(key=lambda line: float(line.split('\t')[2]), reverse=True)

for line in lines:
	print(line, end='')
