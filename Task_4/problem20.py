# Problem: No Idea!
# HackerRank: https://www.hackerrank.com/challenges/no-idea/problem

n, m = map(int, input().split())
array = list(map(int, input().split()))
happy = set(map(int, input().split()))
sad = set(map(int, input().split()))
happiness = 0
for number in array:
    if number in happy:
        happiness += 1
    elif number in sad:
        happiness -= 1
print(happiness)
