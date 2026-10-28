# Problem: Nested Lists
# HackerRank: https://www.hackerrank.com/challenges/nested-list/problem

records = []
for _ in range(int(input())):
    name = input().strip()
    score = float(input())
    records.append((name, score))

second_lowest = sorted({score for _, score in records})[1]
for name, score in sorted(records):
    if score == second_lowest:
        print(name)
