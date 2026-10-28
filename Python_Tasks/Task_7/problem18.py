# Problem: String Construction
# HackerRank: https://www.hackerrank.com/challenges/string-construction/problem

q = int(input().strip())

for _ in range(q):
    s = input().strip()
    print(len(set(s)))
