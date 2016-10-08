# coding: utf-8

with open('col1.txt') as col1_file, \
		open('col2.txt') as col2_file, \
		open('merge.txt', mode='w') as out_file:

	for col1_line, col2_line in zip(col1_file, col2_file):
		out_file.write(col1_line.rstrip() + '\t' + col2_line.rstrip() + '\n')


