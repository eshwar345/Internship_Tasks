# Problem: Tuples
# HackerRank: https://www.hackerrank.com/challenges/python-tuples/problem

n = int(input().strip())
numbers = tuple(map(int, input().split()))

print(hash(numbers))
