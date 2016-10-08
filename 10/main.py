# coding: utf-8

fname = 'hightemp.txt'
count = 0
with open(fname) as data_file:
	for line in data_file:
		count += 1
print(count)
