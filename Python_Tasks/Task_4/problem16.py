# Problem: Nested Lists
# HackerRank: https://www.hackerrank.com/challenges/nested-list/problem

records = []
for _ in range(int(input())):
    name = input().strip()
    score = float(input())
    records.append([name, score])
scores = sorted({score for _, score in records})
second_lowest = scores[1]
for name, score in sorted(records, key=lambda record: record[0]):
    if score == second_lowest:
        print(name)
