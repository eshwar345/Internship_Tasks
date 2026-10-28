# Problem: Alphabet Rangoli
# HackerRank: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string

n = int(input().strip())
alphabet = string.ascii_lowercase
width = 4 * n - 3

for i in range(n - 1, -n, -1):
    level = n - 1 - abs(i)
    left = [alphabet[n - 1 - j] for j in range(level)]
    center = [alphabet[n - 1 - level]]
    row = left + center + left[::-1]
    print("-".join(row).center(width, "-"))
