# Problem: Two Strings
# HackerRank: https://www.hackerrank.com/challenges/two-strings/problem

p = int(input().strip())

for _ in range(p):
    s1 = set(input().strip())
    s2 = set(input().strip())
    print("YES" if s1 & s2 else "NO")
