# Problem: Anagram
# HackerRank: https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter

q = int(input().strip())

for _ in range(q):
    s = input().strip()
    if len(s) % 2:
        print(-1)
    else:
        half = len(s) // 2
        first = Counter(s[:half])
        second = Counter(s[half:])
        print(sum((first - second).values()))
