# Problem: Weighted Uniform Strings
# HackerRank: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

s = input().strip()
n = int(input().strip())
queries = [int(input().strip()) for _ in range(n)]

weights = set()
previous = ""
current_weight = 0

for character in s:
    if character == previous:
        current_weight += ord(character) - ord("a") + 1
    else:
        current_weight = ord(character) - ord("a") + 1
        previous = character
    weights.add(current_weight)

for value in queries:
    print("Yes" if value in weights else "No")
