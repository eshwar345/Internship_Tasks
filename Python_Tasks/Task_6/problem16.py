# Problem: Check Subset
# HackerRank: https://www.hackerrank.com/challenges/py-check-subset/problem

test_cases = int(input().strip())

for _ in range(test_cases):
    n_a = int(input().strip())
    set_a = set(map(int, input().split()))

    n_b = int(input().strip())
    set_b = set(map(int, input().split()))

    print(set_a.issubset(set_b))
