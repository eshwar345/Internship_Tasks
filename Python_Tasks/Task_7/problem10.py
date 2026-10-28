# Problem: CamelCase
# HackerRank: https://www.hackerrank.com/challenges/camelcase/problem

s = input().strip()
print(1 + sum(character.isupper() for character in s) if s else 0)
