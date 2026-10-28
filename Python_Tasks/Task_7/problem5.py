# Problem: Alternating Characters
# HackerRank: https://www.hackerrank.com/challenges/alternating-characters/problem

q = int(input().strip())

for _ in range(q):
    s = input().strip()
    deletions = sum(s[i] == s[i - 1] for i in range(1, len(s)))
    print(deletions)
