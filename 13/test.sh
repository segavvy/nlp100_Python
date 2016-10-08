#!/bin/sh

# マージ
paste col1.txt col2.txt > merge_test.txt

# 比較
diff --report-identical-files merge.txt merge_test.txt

