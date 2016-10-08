# coding: utf-8

fname = 'hightemp.txt'
with open(fname) as data_file:
	for line in data_file:
		print(line.replace('\t', ' '), end='')

