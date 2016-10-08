#!/bin/sh

# 1カラム目でソートし、重複除去して件数付きで出力、その結果をソート
cut --fields=1 hightemp.txt | sort | uniq --count | sort --reverse

