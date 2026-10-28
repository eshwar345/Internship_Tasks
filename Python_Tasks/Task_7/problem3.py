# Problem: Mars Exploration
# HackerRank: https://www.hackerrank.com/challenges/mars-exploration/problem

s = input().strip()
expected = "SOS"
changed = sum(character != expected[i % 3] for i, character in enumerate(s))
print(changed)
