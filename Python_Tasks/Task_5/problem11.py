# Problem: Text Wrap
# HackerRank: https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap

string = input()
width = int(input())
print(textwrap.fill(string, width))
