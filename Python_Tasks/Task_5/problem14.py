# Problem: Finding the Percentage
# HackerRank: https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input())
students = {}
for _ in range(n):
    data = input().split()
    students[data[0]] = list(map(float, data[1:]))

query_name = input().strip()
marks = students[query_name]
print(f"{sum(marks) / len(marks):.2f}")
