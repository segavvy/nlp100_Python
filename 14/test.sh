#!/bin/sh

# Nを入力
echo -n "N--> "
read n

# 切り出し
head --lines=$n hightemp.txt

