# Problem: Set .difference() Operation
# HackerRank: https://www.hackerrank.com/challenges/py-set-difference-operation/problem

n = int(input().strip())
english = set(map(int, input().split()))

m = int(input().strip())
french = set(map(int, input().split()))

print(len(english - french))
