# coding: utf-8

fname = 'hightemp.txt'
with open(fname) as data_file:

	set_ken = set()
	for line in data_file:
		cols = line.split('\t')
		set_ken.add(cols[0])

for n in set_ken:
	print(n)
