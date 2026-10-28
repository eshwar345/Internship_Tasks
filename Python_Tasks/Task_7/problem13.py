# Problem: Sherlock and the Valid String
# HackerRank: https://www.hackerrank.com/challenges/sherlock-and-the-valid-string/problem

from collections import Counter

s = input().strip()
frequencies = list(Counter(s).values())
counts = Counter(frequencies)

if len(counts) == 1:
    print("YES")
elif len(counts) == 2:
    (f1, c1), (f2, c2) = counts.items()
    valid = (
        (f1 == 1 and c1 == 1) or
        (f2 == 1 and c2 == 1) or
        (abs(f1 - f2) == 1 and ((f1 > f2 and c1 == 1) or (f2 > f1 and c2 == 1)))
    )
    print("YES" if valid else "NO")
else:
    print("NO")
