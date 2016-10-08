# coding: utf-8
import gzip
import json
fname = 'jawiki-country.json.gz'

with gzip.open(fname, 'rt') as data_file:
	for line in data_file:
		data_json = json.loads(line)
		if data_json['title'] == 'イギリス':
			print(data_json['text'])
			break
