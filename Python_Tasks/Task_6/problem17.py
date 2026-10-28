# Problem: Check Strict Superset
# HackerRank: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

set_a = set(map(int, input().split()))
n = int(input().strip())

is_strict_superset = True

for _ in range(n):
    other_set = set(map(int, input().split()))
    if not (set_a > other_set):
        is_strict_superset = False

print(is_strict_superset)
