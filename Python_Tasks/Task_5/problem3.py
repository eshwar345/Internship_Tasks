# Problem: Mutations
# HackerRank: https://www.hackerrank.com/challenges/python-mutations/problem

string = input()
position, character = input().split()
position = int(position)
print(string[:position] + character + string[position + 1:])
