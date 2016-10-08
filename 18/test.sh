#!/bin/sh

# 3カラム目を数値として逆順ソート
sort hightemp.txt --key=3,3 --numeric-sort --reverse > result_test.txt

# Pythonのプログラムで実行
python main.py > result.txt

# 結果の確認
diff --report-identical-files result.txt result_test.txt

