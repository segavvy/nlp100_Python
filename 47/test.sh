#!/bin/sh

# 述語でソートして重複除去し、その件数でソート
cut --fields=1 result.txt | sort | uniq --count | sort --numeric-sort --reverse > "predicate.txt"

# 述語と助詞でソートして重複除去し、その件数でソート
cut --fields=1,2 result.txt | sort | uniq --count | sort --numeric-sort --reverse > "predicate_particle.txt"

